from tortoise import fields
from tortoise.models import Model
from cuid import cuid


class BaseModel(Model):
    id = fields.CharField(primary_key=True, max_length=25, default=cuid)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True


class Device(BaseModel):
    port = fields.CharField(null=False, max_length=10, unique=True)
    hwid = fields.CharField(null=False, max_length=50, unique=True)
    manufacturer = fields.CharField(null=False, max_length=50, unique=True)
    serial_number = fields.CharField(null=False, max_length=10, unique=True)

    sector = fields.ForeignKeyField("models.Sector", related_name="devices", null=False)

    def __str__(self):
        return f"Device(id={self.id}, port={self.port}, hwid={self.hwid}, manufacturer={self.manufacturer}, serial_number={self.serial_number})"


class Company(BaseModel):
    name = fields.CharField(null=False, max_length=100)
    cnpj = fields.CharField(null=False, max_length=14, unique=True)

    sectors: fields.ReverseRelation["Sector"]

    def __str__(self):
        return f"Company(id={self.id}, name={self.name}, cnpj={self.cnpj})"


class Sector(BaseModel):
    name = fields.CharField(null=False, max_length=100, unique=True)
    max_idle_time_secs = fields.IntField(default=3600)

    company = fields.ForeignKeyField(
        "models.Company", related_name="sectors", null=False
    )
    devices: fields.ReverseRelation["Device"]
    event_logs: fields.ReverseRelation["EventLog"]

    def __str__(self):
        return f"Sector(id={self.id}, name={self.name})"


class Customer(BaseModel):
    name = fields.CharField(null=False, max_length=100)
    document = fields.CharField(null=False, max_length=30, unique=True)

    orders: fields.ReverseRelation["Order"]

    def __str__(self):
        return f"Customer(id={self.id}, name={self.name}, document={self.document})"


class Order(BaseModel):
    customer = fields.ForeignKeyField(
        "models.Customer", related_name="customers", null=False
    )
    region = fields.IntField(null=False)

    products: fields.ReverseRelation["Product"]

    def __str__(self):
        return f"Order(id={self.id}, customer_id={self.customer_id}, region={self.region})"


class Product(BaseModel):
    name = fields.CharField(null=False, max_length=100)
    width = fields.FloatField(null=False)
    height = fields.FloatField(null=False)
    code = fields.CharField(null=False, max_length=50)

    order = fields.ForeignKeyField("models.Order", related_name="orders", null=False)

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, code={self.code}, order_id={self.order_id})"


class EventLog(BaseModel):
    sector = fields.ForeignKeyField(
        "models.Sector", related_name="event_logs", null=False
    )
    product = fields.ForeignKeyField(
        "models.Product", related_name="products", null=False
    )

    def __str__(self):
        return f"EventLog(id={self.id}, sector_id={self.sector_id}, product_id={self.product_id})"
