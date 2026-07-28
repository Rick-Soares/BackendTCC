from pathlib import Path
import sqlite3
from ast import literal_eval

from models.phone_model import CriarTelefone, Telefone
from models.user_model import Usuario, CriarUsuario
from models.device_model import Device, CriarDevice

BASE_DIR = Path(__file__).resolve().parent
CAMINHO_DATABASE = BASE_DIR.parent / "database" / "data.db"

def abrir_conexao():
    return sqlite3.connect(CAMINHO_DATABASE)

def salvar_usuario(user : Usuario) -> None:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = "INSERT INTO usuarios VALUES (?,?,?,?,?)"
        valores = (str(user.user_id), str(user.nome), str(user.email), str(user.senha_hash), str(user.created_at))

        cursor.execute(comando, valores)

def buscar_usuario_email(email : str) -> Usuario | None:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = """SELECT * FROM usuarios WHERE email = ?"""
        valor = (str(email),)

        cursor.execute(comando, valor)

        resposta = cursor.fetchone()

        if resposta is None:
            return None
        data = CriarUsuario(email=resposta[2],senha=resposta[3],nome=resposta[1])
        return Usuario.criar(data=data, id_usuario=resposta[0], criado_em=resposta[4])

def deletar_usuario_por_email(email : str) -> bool:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = "DELETE FROM usuarios WHERE email = ?"
        valor = (str(email),)

        cursor.execute(comando, valor)

        afetados = cursor.rowcount
        if afetados == 0:
            return False
        return True

def salvar_dispositivo(dispositivo : Device) -> None:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = "INSERT INTO dispositivos VALUES (?,?,?,?,?,?)"
        valores = (str(dispositivo.device_id),
                   str(dispositivo.device_name),
                   str(dispositivo.device_type),
                   str(dispositivo.device_token),
                   str(dispositivo.user_id),
                   str(dispositivo.created_at))

        cursor.execute(comando,valores)

def salvar_telefone(telefone) -> None:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = "INSERT INTO telefones VALUES (?,?,?,?)"
        valores = (str(telefone.telefone_id),
                   str(telefone.numero),
                   str(telefone.user_id),
                   str(telefone.created_at))

        cursor.execute(comando, valores)
        return None

def verificar_telefone(numero) -> bool:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = "SELECT * FROM telefones WHERE numero = ?"
        valor = (str(numero),)

        cursor.execute(comando, valor)

        resposta = cursor.fetchone()
        if resposta is None:
            return True
        return False

def buscar_telefones_por_usuario(user_id) -> list:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = "SELECT * FROM telefones WHERE id_usuario = ?"
        valor = (str(user_id),)
        cursor.execute(comando, valor)

        resposta = cursor.fetchall()
        telefones = []
        for telefone in resposta:
            info = CriarTelefone(numero= telefone[1])
            t = Telefone.criar(data=info, id_telefone=telefone[0], user_id=telefone[2], criado_em=telefone[3])
            telefones.append(t)
        return telefones

def deletar_telefone(telefone_id) -> bool:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()
        comando = "DELETE FROM telefones WHERE id = ?"
        valor = (str(telefone_id),)

        cursor.execute(comando, valor)
        if cursor.rowcount == 0:
            return False
        return True

def buscar_dispositivos_por_usuario(user_id) -> list | None:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = "SELECT * FROM dispositivos WHERE id_usuario = ?"
        valor = (str(user_id),)

        cursor.execute(comando, valor)

        resposta = cursor.fetchall()
        dispositivos = []
        if resposta is None:
            return None
        for dispositivo in resposta:
            info = CriarDevice(device_name=dispositivo[1], device_type=dispositivo[2])
            d = Device.criar(data=info, id_dispositivo=dispositivo[0], token_dispositivo=dispositivo[3], criado_em=dispositivo[5],user_id=dispositivo[4])
            dispositivos.append(d)
        return dispositivos

def busca_dispositivo_por_id(id_dispositivo) -> Device | None:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()
        comando = "SELECT * FROM dispositivos WHERE id = ?"
        valor = (str(id_dispositivo),)

        cursor.execute(comando, valor)

        resposta = cursor.fetchall()
        if resposta is None:
            return None

        for dispositivo in resposta:
            info = CriarDevice(device_name=dispositivo[1], device_type=dispositivo[2])
            d = Device.criar(data=info, id_dispositivo=dispositivo[0], token_dispositivo=dispositivo[3],
                             criado_em=dispositivo[5], user_id=dispositivo[4])
            return  d
    return None

def salvar_alerta(id_alerta, id_dispositivo, id_usuario, data, telefones, nome_dispositivo):
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()
        comando = "INSERT INTO alertas VALUES (?,?,?,?,?,?)"
        valores = (id_alerta, id_dispositivo, id_usuario, data, telefones, nome_dispositivo)

        cursor.execute(comando, valores)

def lista_alertas(id_usuario):
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM alertas WHERE id_usuario = ?",
            (str(id_usuario),)
        )

        resposta = cursor.fetchall()

        alertas = []

        for alerta in resposta:
            alertas.append(
                {
                    "alerta_id": alerta[0],
                    "device_id": alerta[1],
                    "user_id": alerta[2],
                    "timestamp": alerta[3],
                    "telefones_notificados": literal_eval(alerta[4]),
                    "device_name": alerta[5],
                }
            )

        return alertas

