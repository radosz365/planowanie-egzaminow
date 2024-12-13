import csv
import networkx as nx


class Node:
    def __init__(self, course, lecture, group, classrom):
        self.course = course
        self.lecture = lecture
        self.group = group
        self.classrom = classrom

    def __str__(self):
        return f"{self.course} {self.lecture} {self.group} {self.classrom}"


def create_grapf_from_csv(filename):
    G = nx.Graph()
    file_path = "datasets/" + filename

    try:
        with open(file_path, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                course = row[0]
                lecture = row[1]
                group = row[2]
                classrom = row[3]

                node = Node(course, lecture, group, classrom)
                G.add_node(node)

    except FileNotFoundError:
        print("Plik CSV nie został znaleziony.")
    except csv.Error as e:
        print(f"Błąd podczas czytania pliku CSV: {e}")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
    return G
