from web3 import Web3

# Bağlanılacak Ethereum ağına ve Ethereum istemcisine erişim sağlayın
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Özel anahtarınızı ve cüzdan adresinizi kullanarak kimlik doğrulama sağlayın
private_key = 'YOUR_PRIVATE_KEY'
my_address = 'YOUR_WALLET_ADDRESS'

# ERC-20 token sözleşmesi kodu
contract_abi = [...]  # Sözleşme ABI'si
contract_address = 'CONTRACT_ADDRESS'  # Sözleşme adresi

# Sözleşme nesnesini oluşturun
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Token transfer işlemi
recipient_address = 'RECIPIENT_ADDRESS'
amount_to_send = 100  # Göndermek istediğiniz miktar

# Gas fiyatını ve gas limitini ayarlayın
gas_price = w3.toWei('50', 'gwei')  # Örnek bir gas fiyatı
gas_limit = 200000  # Örnek bir gas limiti

# Token gönderme işlemi
transaction = {
    'to': recipient_address,
    'value': 0,
    'gas': gas_limit,
    'gasPrice': gas_price,
    'nonce': w3.eth.getTransactionCount(my_address),
}

# Özel anahtarınızı kullanarak işlemi imzalayın
signed_transaction = w3.eth.account.signTransaction(transaction, private_key)

# İmzalı işlemi ağa gönderin
transaction_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

# İşlem onayını bekleyin
w3.eth.waitForTransactionReceipt(transaction_hash)

print("Token gönderme işlemi tamamlandı.")