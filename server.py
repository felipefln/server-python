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

    n = int(s)
    menos = False
    if s[0] == "-":
        menos = True
        n = -n
    if n == 0:
        return "zero"
    if n  == 100:
        return "menos cem" if menos else "cem"
    if n >= 1000:
        pnm = [n // 1000, n % 1000]
    else:
        pnm = [n]
    psm = []

    i = 0
    for parte in pnm:
        ps = []
        ps.append(c[parte // 100])
        if parte % 100 < 20:
            if len(pnm) == 2 and i == 0 and parte == 1:
                ps.append("")
            else:
                ps.append(u[parte % 100])
        else:
            ps.append(d[(parte % 100) // 10])
            ps.append(u[(parte % 100) % 10])
        res = " e ".join(ps)
        res = re.sub("(^ e | e $)", "", res)
        psm.append(res)
        i += 1

    if len(psm) == 2 and psm[0] == "um":
        psm[0] == ""
    res = " mil e ".join(psm)
    res = re.sub("( e ?$|^ )", "", res)
    return "menos "+res if menos else res


class Server(BaseHTTPRequestHandler):
    def _set_headers(self, cod):
        self.send_response(cod)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_GET(self):
        n = self.path.split("/")[1]
        if is_int(n) and int(n) >= -99999 and int(n) <= 99999:
            self._set_headers(200)
            self.wfile.write(json.dumps({'extenso': extenso(n)}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({}).encode())
        
def run(server_class=HTTPServer, handler_class=Server, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print('Servidor rodando na porta {}...'.format(port))
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
        
