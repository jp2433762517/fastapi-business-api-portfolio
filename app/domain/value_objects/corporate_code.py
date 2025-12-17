from dataclasses import dataclass


@dataclass(frozen=True)
class CorporateCode:
    value: str

    def __post_init__(self):
        if not self.value or len(self.value) < 3:
            raise ValueError("Corporate code must be at least 3 characters")
