import re
import click

# import requests

# TODO: import twitter api
# import tweepy


def validate_email(ctx, param, value):
    ''' Function to validate target\'s email address '''

    try:
        # TODO: create a pattern to match a valid email address
        pattern = re.compile(r'')
        if re.match(pattern, value):
            return value
    except ValueError:
        raise click.BadParameter('You provided an invalid email address')


@click.command()
@click.option('--fullname', prompt='Enter target\'s fullname',
              help='what\'s the target\'s fullname ')
@click.option('--nickname', prompt='Enter target\'s nickname',
              help='Enter target\'s nickname')
@click.option('--email', prompt='Enter target\'s email address',
              help='Enter target\'s email address',
              callback=validate_email)
@click.option('--twitter',
              prompt="What\'s the target\'s twitter handle ?",
              help="What\'s the target\'s twitter handle ?")
@click.option('--facebook',
              prompt="What\'s the target\'s facebook handle ?",
              help="What\'s the target\'s facebook handle ?")
@click.option('--instagram',
              prompt="What\'s the target\'s instagram handle ?",
              help="What\'s the target\'s instagram handle ?")
@click.option('--outfile',
              help='The file containing info obtained about the target',
              default='password.txt', show_default=True)
def pypass(fullname, nickname, email, twitter, instagram, facebook, outfile):
    '''
    Command line password cracker based on user provided information
    '''

    # start by googling the target
    # search the user on facebook using API
    # search the user on instagram using API
    # search the user on twitter using Twitter API
    # its possible the user is on all the platform
    # use the apis to our advantage and get user profile information
    # if target_found:
    # store the details in a file; all possible leads
    # else:
    # click.echo('Target not found')


if __name__ == '__main__':
    pypass()
