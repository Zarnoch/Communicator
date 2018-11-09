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


def perform_test(class_name):
    test_classes = find_all_test_classes()
    if class_name not in test_classes:
        print("Cannot find the test with the following name: {}".format(class_name))
        sys.exit()
    print("Test {} started".format(class_name))
    current_test = test_classes[class_name]()
    current_test.prepare_assumptions()
    for assumption in current_test.assumptions:
        print("Assumtion: {}".format(assumption.description))
    current_test.execute()
    current_test.check_results()


def perform_all_test():
    test_classes = find_all_test_classes()
    for test_class in test_classes:
        perform_test(test_class)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python com_testor.py test_name")
        print("You can type 'all' instead of a test name to perform all tests.")
        sys.exit()
    test_name = sys.argv[1]
    if test_name == "all":
        perform_all_test()
    else:
        perform_test(test_name)



