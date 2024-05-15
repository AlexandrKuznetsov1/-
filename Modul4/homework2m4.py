# 1. Создайте новую функцию def test_function
# 2. Создайте другую функцию внутри функции inner_function,
# функция должна печатать значение "Я в области видимости функции test_function"
# 3. Вызовите функцию inner_function внутри функции test_function
# 4. Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
# inner_function() так как функция находится в локальной области видимости,
# вызвать ее в глобальном пространстве не получится
test_function() # только через вызов объемлющей функции