from sqlmodel import Session
from models.address import Address, AddressCreate, AddressUpdate
from models.user import User
from fastapi import HTTPException


def create_address_for_user(user_id: int, address_in: AddressCreate, session: Session):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    address = Address(
        user_id = address_in.user_id,
        street=address_in.street,
        city=address_in.city,
        postal_code=address_in.postal_code,
        country=address_in.country,
    )

    session.add(address)
    session.commit()
    session.refresh(address)
    return address


def update_address(user_id: int, address_in: AddressUpdate, session: Session) -> Address:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not user.address:
        raise HTTPException(status_code=404, detail="Address not found")

    address = user.address

    if address_in.street is not None:
        address.street = address_in.street
    if address_in.city is not None:
        address.city = address_in.city
    if address_in.postal_code is not None:
        address.postal_code = address_in.postal_code
    if address_in.country is not None:
        address.country = address_in.country

    session.commit()
    session.refresh(address)
    return address
