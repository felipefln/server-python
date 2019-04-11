from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re

def is_int(s):
    return s.isdigit() or (s.startswith('-') and s[1:].isdigit())

def extenso(s):
    u = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
         "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
         "dezoito", "dezenove"]
    d = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta",
         "setenta", "oitenta", "noventa"]
    c = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos",
         "setecentos", "oitocentos", "novecentos" ]

   