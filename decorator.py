def print_num_gt(gt_value):
    def decorator(func):
        def wrapper(x):
            if x > gt_value:
                print(x)
            else:
                print("error")
        return wrapper
    return decorator


@print_num_gt(3)
def print_num(x: int):
    print(x)


if __name__ == '__main__':
    print_num()  # Подставьте свое значение
