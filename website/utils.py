from website.models import Project


def create_project():
    numbers = [a, b, c, d, e]

    def get_project_image(number):
        number_repr = ""
        for number_index, number_name in Project.name:
            if number == number_index:
                number_repr = number_name
                break

        return "project_{}.jpg".format(number_repr)

    projects = [Project(name=name, image=get_project_image(number), description=description) for number in numbers]

    Project.objects.bulk_create(projects)