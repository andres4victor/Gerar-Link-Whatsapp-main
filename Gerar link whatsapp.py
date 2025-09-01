import pyperclip
def gerar_link(numero, texto):
  
  url_base = "https://wa.me/"
  numero_formatado = f"{numero}"
  texto_formatado = f"?text={texto.replace(' ', '%20')}"
  link_completo = url_base + numero_formatado + texto_formatado
  return link_completo
def main():
  numero_whatsapp = input("Digite o número de WhatsApp: ")
  texto_inicial = input("Digite a mensagem inicial (opcional): ")
  link_gerado = gerar_link(numero_whatsapp, texto_inicial)
  print(f"Link gerado: {link_gerado}")
  pyperclip.copy(link_gerado)
  print("Link copiado para a área de transferência.")
  outro_link = input("Deseja gerar outro link? (Sim/Não): ")
  while outro_link.lower() == "sim":
    numero_whatsapp = input("Digite o novo número de WhatsApp: ")
    texto_inicial = input("Digite a mensagem inicial (opcional): ")
    link_gerado = gerar_link(numero_whatsapp, texto_inicial)
    print(f"Link gerado: {link_gerado}")
    pyperclip.copy(link_gerado)
    print("Link copiado para a área de transferência.")
    outro_link = input("Deseja gerar outro link? (Sim/Não): ")
  print("Programa finalizado.")
if __name__ == "__main__":
  main()
