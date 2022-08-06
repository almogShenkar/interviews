import click

# A datastore interactive cli with click lib


def set_value(dict_obj, k, v):
    dict_obj[k] = v


def get_value(dict_obj, k):
    return dict_obj.get(k)


def delete_value(dict_obj, k):
    del dict_obj[k]


@click.command('datastore')
def datastore(**kwargs):
    action = input("Please enter: set/get/delete/stop:\n")

    while action != 'stop':
        print(f'Data before action: {kwargs}')
        k = input("key:")

        if action == 'set':
            v = input("value:")
            set_value(kwargs, k, v)

        elif action == 'get':
            print(get_value(kwargs, k))

        elif action == 'delete':
            delete_value(kwargs, k)

        else:
            print('unsupported action. try again')

        print(f'Data After: {kwargs}')
        action = input("Please enter: set/get/delete/stop:\n")


if __name__ == '__main__':
    datastore()
