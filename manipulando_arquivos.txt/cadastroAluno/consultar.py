def header():
    print("---------------------------------------------------------------------------")
    print("----------------------------- Consultar Aluno -----------------------------")
    print("---------------------------------------------------------------------------")


def situation(media):
    if float(media) >= 7:
        return "APROVADO"
    elif float(media) > 4:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"


def calculate_average(nota1, nota2, nota3, nota4):
    media = (float(nota1) + float(nota2) + float(nota3) + float(nota4))/4
    return media


def consult_student_data():
    header()
    print("{:<9} | {:<9} | {:<6} | {:<6} | {:<6} | {:<6} | {:<6} | {:<6}"
          .format("NOME", "MATRICULA", "1ªNOTA", "2ªNOTA", "3ªNOTA", "4ªNOTA", "MEDIA", "SITUAÇÃO"))
    print("---------------------------------------------------------------------------")
    with open("file_student_data.txt", "r") as file:
        data_file = file.readlines()
        for x in data_file:
            student = x.split(" - ")
            media = calculate_average(student[2], student[3], student[4], student[5])
            student_situation = situation(media)
            print("{:<9} | {:<9} | {:<6} | {:<6} | {:<6} | {:<6} | {:<6} | {:<6}"
                  .format(student[0], student[1], float(student[2]), float(student[3]),
                          float(student[4]), float(student[5]), media, student_situation))
