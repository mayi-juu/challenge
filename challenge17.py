# 3. reモジュールを使って、何かの文字の後にoが2回登場する単語に一致する正規表現を書く。
# そして、"The ghost that says boo haunts the loo"の文中にあるbooやlooに一致するか試す。

import re

g="The ghost that says boo haunts a loo"
G=re.findall(".oo",g)
print(G)

b1=re.findall(" . ",g,re.IGNORECASE)
print(b1)

b2=re.findall(" .* ",g,re.IGNORECASE)
print(b2)

b3=re.findall(" .*? ",g,re.IGNORECASE)
print(b3)