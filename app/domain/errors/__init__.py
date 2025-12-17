class DomainError(Exception):
    pass


class UserNotFoundError(DomainError):
    pass


class InvalidCredentialsError(DomainError):
    pass


class EmailAlreadyExistsError(DomainError):
    pass
