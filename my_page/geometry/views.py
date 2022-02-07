from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


def get_rectangle_area(request, width: int, height: int):
    area = width * height
    return HttpResponse(f'The area of the {width}x{height} rectangle is {area}!')


def get_rectangle_area_error(request, width, height):
    return HttpResponseNotFound('Please, enter valid values!')

def redirect_rectangle_area(request, width: int, height: int):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def get_square_area(request, width: int):
    area = width ** 2
    return HttpResponse(f'The area of the {width}x{width} square is {area}!')


def get_square_area_error(request, width):
    return HttpResponseNotFound('Please, enter valid value!')

def redirect_square_area(request, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')

def get_circle_area(request, radius: int):
    PI = 3.14
    area = 2 * PI * radius
    return HttpResponse(f'The area of the circle with {radius} radius is ~ {area}!')


def get_circle_area_error(request, radius):
    return HttpResponseNotFound('Please, enter valid value!')

def redirect_circle_area(request, radius: int):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')