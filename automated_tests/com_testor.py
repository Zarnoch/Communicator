import sys
import inspect
import pkgutil


def find_all_test_classes():
    clsmembers = {}
    module_names = ([name for _, name, _ in pkgutil.iter_modules(['test_cases'])])
    for module_name in module_names:
        full_module_name = "test_cases.{}".format(module_name)
        for name, obj in inspect.getmembers(__import__(full_module_name)):
            clsmembers.update([m for m in inspect.getmembers(obj, inspect.isclass) if m[1].__module__ == full_module_name])
    return clsmembers


def perform_test(test_name):
    '''Wypisanie jakie test sie rozpoczal '''
    print("Test {} started".format(test_name))

    '''Inicjalizacja testu podanego w args '''
    current_test = test_classes[test_name]()

    '''Przygotowanie assumptions z testu'''
    current_test.prepare_assumptions()

    '''Opcjonalinie: Wypisanie assumptions '''
    for assumption in current_test.assumptions:
        print("Assumtion: {}".format(assumption.description))

    '''Egzekucja metody /Execution/'''
    current_test.execute()

    '''Sprawdzenie wynikow poprzez metode z klasy testu /CheckResults/'''
    current_test.check_results()


# Gather all test classes
test_classes = find_all_test_classes()
test_name = sys.argv[1]

perform_test(test_name)



