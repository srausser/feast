from typing import Optional

from pydantic import StrictStr

from feast.repo_config import FeastConfigBaseModel


class PostgreSQLConfig(FeastConfigBaseModel):
    host: StrictStr
    port: int = 5432
    database: StrictStr
    db_schema: StrictStr = "public"
    user: StrictStr
    password: StrictStr
    sslmode: Optional[StrictStr] = None
    sslkey_path: Optional[StrictStr] = None
    sslcert_path: Optional[StrictStr] = None
    sslrootcert_path: Optional[StrictStr] = None
    pass_search_path_to_connector: bool = True
