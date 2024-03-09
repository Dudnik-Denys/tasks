from threading import local


def print_msg(stor_local: local) -> None:
    msg = getattr(stor_local, "msg", "failure")
    fileno = getattr(stor_local, "fileno", "failure")
    permission = getattr(stor_local, "permission", "guest")
    print(f"{msg}, {fileno=}, {permission}")
