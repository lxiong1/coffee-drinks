"""Location for static methods that are used for validation purposes"""

from uuid import UUID


class Validator:
    """Static class for validation-related methods"""

    @staticmethod
    def validate_uuid4(uuid_string: str) -> bool:
        """Returns True or False depending on checked version of given UUID string

        Args:
            uuid_string (str): UUID to be checked against a specific UUID version 4

        Returns:
            bool: True or False
        """
        try:
            uuid_comparison = UUID(uuid_string, version=4)
        except ValueError:  # pragma: no cover
            return False

        return str(uuid_comparison) == uuid_string
