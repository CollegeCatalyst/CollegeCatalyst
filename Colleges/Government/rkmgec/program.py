from os import write
i=int(input('Enter serial number::'))
n=input('Enter Mess name:::')
j=input('Enter ratings:::')
x=input('Enter location::::')
with open(f"mess.txt","a") as f:
    f.write(f'''
    <tr style="height: 46px;" class="tdata">

                    <td style="text-align: center; width: 5%;">{i}</td>

                    <td style="width: 40%;">{n}</td>

                    <td style="width: 30%;"><span style="font-size: 14px;"class='ratings'>
                            {j}
                        </span></td>
                    <td style="width: 25%;">
                        <span style="font-size: 14px;">
                            <a title="View" href="{x}" target="_blank"
                                rel="noopener">View</a></span>
                    </td>
    </tr>''')
    f.close()
    
