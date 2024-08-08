def zenit_polar_replace(text):
    #Aplicar a codificação Z-E-N-I-T P-O-L-A-R utilizando o método replace
    replacements = [('z','p'), ('e','o'), ('n','l'), ('i','a'), ('t','r'),
                    ('Z','P'), ('E','O'), ('N','L'), ('I','A'), ('T','R')]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def main():
    
    # Entrada da frase e aplicação de codificação
    frase = "It's not natural. I personally don't think it would be cool because that's not what skating is. Skating is an expression of yourself you know?"
    frase_titulo = frase.title() #Primeira letra de cada palavra
    
    # Dividir a frase em palavras
    palavras = frase_titulo.split()
    
    # Processar cada palavra na lista usando ZENIT POLAR
    coded_palavra = [zenit_polar_replace(palavra) for palavra in palavras]
    
    # Juntar todas as palavras codificadas em uma frase
    coded_frase = " ".join(coded_palavra)
    print("Original: ", frase)
    print("Titulo: ", frase_titulo)
    print("Coded: ", coded_frase)
    
if __name__ == '__main__':
    main()
    