import pickle

# Load trained model
with open("model/phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

print("\n🛡️ Phishing Website Detection System 🛡️")

# Exact feature order from dataset
columns = [
    'id',
    'having_IP_Address',
    'URL_Length',
    'Shortining_Service',
    'having_At_Symbol',
    'double_slash_redirecting',
    'Prefix_Suffix',
    'having_Sub_Domain',
    'SSLfinal_State',
    'Domain_registeration_length',
    'Favicon',
    'port',
    'HTTPS_token',
    'Request_URL',
    'URL_of_Anchor',
    'Links_in_tags',
    'SFH',
    'Submitting_to_email',
    'Abnormal_URL',
    'Redirect',
    'on_mouseover',
    'RightClick',
    'popUpWidnow',
    'Iframe',
    'age_of_domain',
    'DNSRecord',
    'web_traffic',
    'Page_Rank',
    'Google_Index',
    'Links_pointing_to_page',
    'Statistical_report'
]

while True:
    print("\nEnter website features:")

    features = []
    for col in columns:
        value = int(input(f"{col}: "))
        features.append(value)

    prediction = model.predict([features])

    if prediction[0] == 1:
        print("\n✅ This website is LEGITIMATE")
    else:
        print("\n⚠️ This website is PHISHING")

    choice = input("\nCheck another website? (y/n): ")
    if choice.lower() != 'y':
        break
