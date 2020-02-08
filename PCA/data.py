data = {'elf':[
                {'box1':[{"W":["DATE&TIME_W"]}
                        ,{"D":["DATE&TIME_D"]}
                        ]
                },
                {'box2':[{"W":["DATE&TIME_W"]}
                        ,{"D":["DATE&TIME_D"]}
                        ]
                },
                {'box3':[{"W":["DATE&TIME_W"]}
                        ,{"D":["DATE&TIME_D"]}
                        ]
                },{'box4':[{"W":["DATE&TIME_W"]}
                        ,{"D":["DATE&TIME_D"]}
                        ]
                }
               ]

        }
a = data['elf'][0]['box1']
print(a)
lst_word = ['elf','box1']
b = data[lst_word[0]][0][lst_word[1]]
# lst_label = [label['text'],label2['text'],label3['text'],label4['text']]
# lst_final_str = [final_str,final_str2,final_str3,final_str4]
print(a == b)