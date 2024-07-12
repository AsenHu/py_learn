print("My friend very like Pmarusama, so I create this file.")

names = ['Natsume_Iroha', 'Asagi_Mutsuki',
         'Shishidou_Izumi', 'Nakamasa_Ichika']
print(names)

cant_coming = 'Nakamasa_Ichika'
names.remove(cant_coming)
print(f'{cant_coming.title()} can not coming to the party.')
names.append('Kurimura_Airi')
print(names)

print("I found a bigger table, so I can invite more friends.")
names.insert(0, 'Asagao_Hanae')
names.insert(2, 'Shirasu_Azusa')
names.append('Utazumi_Sakurako')
print(f'Welcome to the party, {names[0]}, {names[2]} and {names[-1]}.')

print("Sorry, I can only invite two friends.")
while len(names) > 2:
    sorry = names.pop()
    print(f"Sorry, {sorry}.")
print(names)

for name in names:
    print(f"{name}, please come to the party.")

print("The party is over.")
del names[0]
del names[0]
print(names)
