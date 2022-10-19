def pegar_dados(self):
    path = 'C:\Comprovante_08-10-2022_060323.pdf'

    lista = []
    index_lista = 0

    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        page_content = pdf.getPage(0).extractText()

        # print(page_content)

        pos_termino = page_content.find('S A L D O')
        pos = 0

        print(page_content, "\n")
        while pos < pos_termino - 13:
            if page_content[pos:pos + 3] == "(-)" or page_content[pos:pos + 3] == "(+)":
                pos_aux = pos - 2
                while page_content[pos_aux] != "\n":
                    pos_aux -= 1
                valor = page_content[pos_aux + 1:pos - 1]
                dia = page_content[pos + 3:pos + 13]
                sinal = page_content[pos:pos + 3]

                pos_aux = pos + 13
                while page_content[pos_aux] != "\n":
                    pos_aux += 1
                historico = page_content[pos + 13:pos_aux]

                lista.insert(index_lista, [dia, sinal, historico, valor])
                index_lista += 1

            pos += 1

        for linha in range(0, len(lista)):
            print(lista[linha][0], "\t", lista[linha][1], "\t", lista[linha][2], lista[linha][3], "\n")