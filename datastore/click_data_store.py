import click
import json

# File path for storing the datastore
DATASTORE_FILE = "db_datastore/datastore.json"


# Function to load the datastore from a JSON file
def load_datastore():
    try:
        with open(DATASTORE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# Function to save the datastore to a JSON file
def save_datastore(datastore):
    with open(DATASTORE_FILE, 'w') as f:
        json.dump(datastore, f)


# Function to set a key-value pair in the datastore
def set_value(datastore, key, value):
    datastore[key] = value


# Function to retrieve the value associated with a given key from the datastore
def get_value(datastore, key):
    return datastore.get(key)


# Function to remove a key-value pair from the datastore
def delete_value(datastore, key):
    del datastore[key]


# Create a Click group for the CLI application
@click.group()
@click.pass_context
def cli(ctx):
    """A CLI for interacting with a key-value datastore."""
    # Load the datastore from the JSON file and pass it to commands
    ctx.obj = load_datastore()


# Command to set a key-value pair in the datastore
@cli.command()
@click.argument('key')
@click.argument('value')
@click.pass_context
def set(ctx, key, value):
    """Set a key-value pair in the datastore."""
    set_value(ctx.obj, key, value)
    save_datastore(ctx.obj)
    click.echo(f"Set '{key}' to '{value}'")


# Command to retrieve the value associated with a given key from the datastore
@cli.command()
@click.argument('key')
@click.pass_context
def get(ctx, key):
    """Retrieve the value associated with a given key from the datastore."""
    value = get_value(ctx.obj, key)
    click.echo(value)


# Command to remove a key-value pair from the datastore
@cli.command()
@click.argument('key')
@click.pass_context
def delete(ctx, key):
    """Remove a key-value pair from the datastore."""
    delete_value(ctx.obj, key)
    save_datastore(ctx.obj)
    click.echo(f"Deleted '{key}'")


# Entry point for the CLI application
if __name__ == '__main__':
    cli()
