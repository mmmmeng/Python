ControlFocus("�ļ��ϴ�","","Edit1")  ;ControlFocus("title","text",controlID) Edit1=Edit instance 1  ����ʶ��window����

WinWait("[CLASS:#32770]","",10) ;wait 10 seconds for the Upload window To appear

ControlSetText("�ļ��ϴ�","","Edit1","C:\\Users\\lixc\\Desktop\\data.txt") ;set the file name text on the Edit field
Sleep(2000)

ControlClick("�ļ��ϴ�","","Botton1") ;click on the open button