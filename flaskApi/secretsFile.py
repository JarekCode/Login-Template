# Private items
items = {
  # NOTE: "appConfigSecretKey"
  #       Use 'secrets.token_hex(16)' to generate it.
  "appConfigSecretKey": "",

  # NOTE: "mailServer"
  "mailServer": "",
  # NOTE: "mailPort"
  "mailPort": 587,
  # NOTE: "mailEmail"
  "mailEmail": "",
  # NOTE: "mailUsername"
  "mailUsername": "",
  # NOTE: "mailPassword"
  "mailPassword": "",
}

# Return specified item
def getItem(key):
  try:
    return items.get(key)
  except:
    return "KEY_ERROR"