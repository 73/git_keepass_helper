git-keepass-helper
==================

A KeePass crendential helper for git

## REQUIREMENTS
- Python 3
- A [KeePass](https://keepassxc.org) database file (.kdbx)

## INSTALL
```sh
pip3 install --user git+https://github.com/73/git_keepass_helper#egg=git_keepass_helper
```

## USAGE
To connect a kdbx file with a repository (or your machine's git configuration):

```sh
git config [--global] credential.helper 'keepass /path/to/your.kdbx'
```

## TODO
1. Implement store
2. Implement erase
3. Ask nicer for the password
4. Put it on PyPi
