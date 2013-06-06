#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3



def connect():
    con = sqlite3.connect('productos.db')
    con.row_factory = sqlite3.Row
    return con


def get_marcas():
    con = connect()
    c = con.cursor()
    query = """SELECT id_marca, nombre FROM marcas"""
    result = c.execute(query)
    marcas = result.fetchall()
    con.close()
    return marcas

def get_productos():
    con = connect()
    c = con.cursor()
    query = """SELECT a.codigo, a.nombre, a.descripcion, a.color, a.precio, b.nombre as 'marca'
            FROM productos a, marcas b WHERE a.fk_id_marca = b.id_marca"""
    result = c.execute(query)
    productos = result.fetchall()
    con.close()
    return productos

def get_productos_por_marca(id_marca):
    con = connect()
    c = con.cursor()
    query = """SELECT a.codigo, a.nombre, a.descripcion, a.color, a.precio, b.nombre as 'marca'
            FROM productos a, marcas b WHERE a.fk_id_marca = b.id_marca
            AND a.fk_id_marca = ?"""
    result = c.execute(query, [id_marca])
    productos = result.fetchall()
    con.close()
    return productos

def search_productos(word):
    con = connect()
    c = con.cursor()
    query = """SELECT a.codigo, a.nombre, a.descripcion, a.color, a.precio, b.nombre as 'marca'
            FROM productos a, marcas b WHERE a.fk_id_marca = b.id_marca
            AND (a.nombre LIKE '%'||?||'%')"""

    result = c.execute(query, [word])
    productos = result.fetchall()
    con.close()
    return productos

def delete(codigo):
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM productos WHERE codigo  = ?"
    try:
        resultado = c.execute(query, [codigo])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def agregar(codigo,nombre,descripcion,color,precio):
    exito = False
    con = connect()
    c = con.cursor()
    values = [codigo,nombre,descripcion,color,precio]
    query = "INSERT INTO productos (codigo, nombre, descripcion, color, precio) VALUES (?,?,?,?,?)"
    try:
        resultado = c.execute(query, values)
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito










    


