KV = '''

ScreenManager:
    Nav:
    Add:
    Profile:
    setting:
    Edit:
    Password:
    WelcomeScreen:
    UsernameScreen:
    DOB:
    MainScreen:
    contactus:
    Feedback:
#------------------------------------------------------------- Nav Screen ------------------------------------------------------------------------
<Nav>
    name: '1s'
    FitImage:
        source:'main.jpg'
        opacity: 0.2
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "120dp", "80dp"
        pos_hint: {"center_x":0.15, "center_y":0.79}
        elevation:'8dp'

        MDLabel:
            id : rrr
            text: root.priceTracker()
            theme_text_color: "Primary"
            pos_hint: {"center_x":0.60, "center_y":0.99}
            height: self.texture_size[1]

    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "120dp", "80dp"
        pos_hint: {"center_x":0.5, "center_y":0.79}
        elevation:'8dp'

        MDLabel:
            id : sss
            text: root.priceTracker1()
            theme_text_color: "Primary"
            halign:'center'
            pos_hint: {"center_x":0.50, "center_y":0.99}
            height: self.texture_size[1]

    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "120dp", "80dp"
        pos_hint: {"center_x":0.85, "center_y":0.79}
        elevation:'8dp'

        MDLabel:
            id : ooo
            text: root.cv()
            halign : 'center'
            theme_text_color: "Primary"
            pos_hint: {"center_x":0.50, "center_y":0.99}
            height: self.texture_size[1]



    BoxLayout:
        orientation:'vertical'
        pos_hint: {'center_x':0.50,'center_y':0.20}
        MDCard:
            orientation: "vertical"
            padding: "8dp"
            size_hint: None, None
            size: "400dp", "40dp"
            pos_hint: {"center_x":0.50, "center_y":0.95}
            elevation:'8dp'

            MDLabel:
                text: "Portfolio"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]


        ScrollView:
            MDList:
                id: dock     

    MDFloatingActionButton:
        icon  : "plus"
        elevation_normal : 12
        on_press : root.manager.current='add'
        pos_hint: {"center_x":0.9, "center_y":0.15}
        text_color: 0,0,1,1
        elevation : '8dp'


    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: "Stockerr  "
            elevation : '8dp'
            left_action_items : [['menu' , lambda x : nav_drawer.set_state("open")]]

        Widget:

    MDNavigationDrawer:
        id : nav_drawer
        BoxLayout:
            orientation : 'vertical'
            spacing : '8dp'
            padding : '8dp'

            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: 'Profile'
                        on_release: root.manager.current = 'pro'
                        IconLeftWidget:
                            icon : 'account-details'
                    OneLineIconListItem:
                        text: 'Settings'
                        on_release: root.manager.current = 's'
                        IconLeftWidget:
                            icon : "cogs"  
                    OneLineIconListItem:
                        text: 'Logout'
                        on_release: root.manager.current = 'welcomescreen'
                        IconLeftWidget:
                            icon : 'logout'
                    OneLineIconListItem:
                        text: 'Contact us'
                        on_release: root.manager.current = 'cu'
                        IconLeftWidget:
                            icon : 'chat'
                    OneLineIconListItem:
                        text: 'Feedback'
                        on_release: root.manager.current = 'fb'
                        IconLeftWidget:
                            icon : 'star'
#-------------------------------------------------------- Add Screen -------------------------------------------------------
<Add>
    name: 'add'
    FitImage:
        source:'main1.jpg'
        opacity: 0.2
    MDRaisedButton:
        text: "Save"
        elevation: 12
        size_hint: (0.2,0.08)
        font_size: '20sp'
        pos_hint: {'center_x':0.6,'center_y':0.95}
        size_hint_x: None
        width:300
        text_color: 1, 1, 0, 1
        on_press: app.savestock()
        on_release: app.showstock1()

    MDRaisedButton:
        text: "Cancel"
        elevation_normal : 12
        size_hint: (0.22,0.08)
        font_size: '20sp'
        pos_hint: {'center_x':0.85,'center_y':0.95}
        size_hint_x: None
        width:300
        text_color : 1,1,0,1
        on_press:
            root.manager.current = '1s'
    
    MDLabel:
        text: "ADD STOCKS"
        font_size: '20sp'
        pos_hint: {'center_x':0.18,'center_y':0.97}
        halign: "center"
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        size_hint_x: None
        width:300
   
    MDTextField:
        id: company
        hint_text: "Company Name"
        helper_text: "Text is always here"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.43, "center_y":0.85}
        size_hint_x: None
        width:300
        required: True

    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "310dp", "60dp"
        pos_hint: {"center_x":0.43, "center_y":0.70}
        elevation: '10dp'
        
        MDLabel:
            text: "Company's Current Price"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDLabel:
            id: current_price
            text: "abc"

    MDTextField:    
        id: invest
        hint_text: "Investment Price"
        helper_text: "Text is always here"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.43, "center_y":0.55}
        size_hint_x: None
        width:300
        required: True

    MDTextField:   
        id: quantity
        hint_text: "Quantity"
        helper_text: "Text is always here"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.43, "center_y":0.40}
        size_hint_x: None
        width:300
        required: True
#--------------------------------------------------- Profile Screen --------------------------------------------------------------
<Profile>
    name: 'pro'
    MDCard:
        orientation: "horizontal"
        padding: "8dp"
        size_hint: None, None
        size: "400dp", "60dp"
        pos_hint: {"center_x":0.50, "center_y":0.95}
        elevation: '10dp'

        MDIconButton:
            icon: "arrow-left"
            size_hint_y: None
            pos_hint: {"center_x":0.50, "center_y":0.48}
            on_press : root.manager.current = '1s'

        MDLabel:
            text: " Your Profile"
            theme_text_color: "Primary"
            size_hint_y: None
            pos_hint: {"center_x":0.50, "center_y":0.48}
            height: self.texture_size[1]

    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "400dp", "80dp"
        pos_hint: {"center_x":0.50, "center_y":0.78}
        elevation: '10dp'

        MDLabel:
            text: "username"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "1dp"

        MDLabel:
            id: uname
            text: ""

    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "400dp", "80dp"
        pos_hint: {"center_x":0.50, "center_y":0.58}
        elevation: '10dp'

        MDLabel:
            text: "Email ID"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "1dp"

        MDLabel:
            id: uemail
            text: " "

    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "400dp", "80dp"
        pos_hint: {"center_x":0.50, "center_y":0.38}
        elevation: '10dp'

        MDLabel:
            text: "phone"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "1dp"

        MDLabel:
            id: uphone
            text: " "




#-------------------------------------------------------- Settings Screen ----------------------------------------------------------------------
<setting>
    name:'s'
    BoxLayout:
        orientation:'vertical'
        pos_hint: {"center_x":0.55, "center_y":0.4}
        width : 300


        Widget:

    Screen :

        ScrollView:
            MDList:

                OneLineAvatarIconListItem:
                    text: "Change Theme"
                    on_size:
                        self.ids._right_container.width = container.width
                        self.ids._right_container.x = container.width

                    IconLeftWidget:
                        icon: "brightness-6"


                    Container:
                        id: container

                        MDFloatLayout:

                        MDSwitch:
                            pos_hint: {"center_x":0.5, "center_y":.6}
                            width: dp(45)
                            on_active: app.check(*args)

                OneLineIconListItem:
                    text: 'Edit Profile'
                    width : 300
                    on_release: root.manager.current = 'edit'
                    IconLeftWidget :
                        icon : "account-arrow-right"


                OneLineIconListItem:
                    text: 'Change Password'
                    width : 300
                    on_release: root.manager.current = 'password'
                    IconLeftWidget:
                        icon: "eye-plus"



        Screen :

        MDRaisedButton:
            text: "Back"
            width : 300
            elevation : 12
            font_size: '20sp'
            pos_hint: {"center_x": 0.8, "center_y": 0.2}
            text_color: 1, 1, 0, 1
            on_release: root.manager.current = '1s'
#----------------------------------------------------------- Edit Screen -----------------------------------------------------------------------------------------------------      
<Edit>
    name : 'edit' 
    BoxLayout:
        orientation:'vertical'
        pos_hint: {"center_x":0.55, "center_y":0.4}
        width : 300
        spacing:'20dp'
        padding: "45dp"


    Screen :

        MDLabel:
            text : "Username"
            pos_hint :{"center_x":.6,"center_y":.9}

        MDTextField:
            id: username
            mode : "rectangle"
            icon_right:"account"
            hint_text:"Enter Username      "
            helper_text_mode:"on_focus"
            helper_text: "Always write here"
            size_hint_x: None
            pos_hint : {"center_x":.5,"center_y":.82}
            width:300
            required: True

        MDLabel:
            text : "Email"
            pos_hint :{"center_x":.6,"center_y":.7}

        MDTextField:
            id: email
            mode : "rectangle"
            icon_right:"email"
            hint_text:"Enter E-mail Id      "
            helper_text_mode:"on_focus"
            helper_text: "Always write here"
            size_hint_x: None
            pos_hint : {"center_x":.5,"center_y":.62}
            width:300
            required: True

        MDLabel:
            text : "Contact No."
            pos_hint :{"center_x":.6,"center_y":.5}

        MDTextField:
            id:contact
            mode : "rectangle"
            icon_right:"phone"
            hint_text:"Enter Phone No.      "
            helper_text_mode:"on_focus"
            helper_text: "Enter 10 digit Phone No."
            size_hint_x: None
            pos_hint : {"center_x":.5,"center_y":.42}
            width:300
            max_text_length:10
            required: True

        MDRaisedButton:
            text: "Back"
            width : 300
            elevation : 12
            font_size: '20sp'
            pos_hint: {"center_x": 0.8, "center_y": 0.2}
            text_color: 1, 1, 0, 1
            on_release: root.manager.current = 's'

        MDRaisedButton:
            text: "Save"
            width : 300
            elevation : 12
            font_size: '20sp'
            pos_hint: {"center_x": 0.8, "center_y": 0.3}
            text_color: 1, 1, 0, 1
            on_press: root.saveprofile()

#------------------------------------------------------- Password Screen ------------------------------------------------------------
<Password>
    name:'password'
    BoxLayout:
        orientation:'vertical'
        pos_hint: {"center_x":0.55, "center_y":0.4}
        width : 300
        spacing:'20dp'
        padding: "45dp"

    Screen :

    MDLabel:
        text : "Current Password"
        pos_hint :{"center_x":.6,"center_y":.9}

    MDTextField:
        id: cur_pass
        mode : "rectangle"
        icon_left: 'key-variant'
        icon_right: 'eye-off'
        hint_text: 'Password    '
        helper_text:"Text is always here"
        helper_text_mode:"on_focus"
        password : True
        size_hint_x: None
        width:300
        pos_hint : {"center_x":.5,"center_y":.82}
        required: True

    MDLabel:
        text : "New Password"
        pos_hint :{"center_x":.6,"center_y":.7}

    MDTextField:
        id: new_pass
        mode : "rectangle"
        icon_left: 'key-variant'
        icon_right: 'eye-plus'
        hint_text: 'Enter Password    '
        helper_text:"Text is always here"
        helper_text_mode:"on_focus"
        password : True
        size_hint_x: None
        width:300
        pos_hint : {"center_x":.5,"center_y":.62}  
        required: True

    MDLabel:
        text : "Confirm Password"
        pos_hint :{"center_x":.6,"center_y":.5}

    MDTextField:
        id: con_pass
        mode : "rectangle"
        icon_left: 'key-variant'
        icon_right: 'eye-check'
        hint_text: 'Enter Password    '
        helper_text:"Text is always here"
        helper_text_mode:"on_focus"
        password : True
        size_hint_x: None
        width:300
        pos_hint : {"center_x":.5,"center_y":.42}
        required: True

    MDRaisedButton:
        text: "Back"
        width : 300
        elevation : 12
        font_size: '20sp'
        pos_hint: {"center_x": 0.8, "center_y": 0.2}
        text_color: 1, 1, 0, 1
        on_release: root.manager.current = 's'

    MDRaisedButton:
        text: "Save"
        width : 300
        elevation : 12
        font_size: '20sp'
        pos_hint: {"center_x": 0.8, "center_y": 0.3}
        text_color: 1, 1, 0, 1
        on_press: root.changepass()
#--------------------------------------------------------- Welcome Screen -----------------------------------------------------  
<WelcomeScreen>:
    name : 'welcomescreen'
    
    MDLabel:
        text:'Get Started With Stocker'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_y':0.65}
    MDFloatingActionButton:
        icon:'account-arrow-right-outline'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '60sp'
        pos_hint: {'center_x':0.5,'center_y':0.15}
        on_press:
            root.manager.current = 'usernamescreen'
    MDProgressBar:
        value:30
        pos_hint:{'center_y' : 0.04}
#------------------------------------------------------ Username Screen ---------------------------------------------------------------------------
<UsernameScreen>
    name:'usernamescreen'

    FitImage:
        source:'signupbg.jpg'
        opacity: 0.2
    MDFloatingActionButton:
        icon: 'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'welcomescreen'
    MDFloatingActionButton:
        id:disabled_button
        disabled: True
        icon: 'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'dob'
    MDProgressBar:
        value:60
        pos_hint: {'center_y':0.02}
    MDLabel:
        text:'Enter username and password'
        text_color: 1, 1, 1, 1
        font_style: 'H4'
        halign: 'center'
        pos_hint : {'center_y':0.85}
    MDTextField:
        id:username_text_fied
        pos_hint: {'center_x':0.5,'center_y':0.6}
        size_hint: (0.7,0.1)
        hint_text : 'username'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDTextField:
        id:pw_text
        pos_hint: {'center_x':0.5,'center_y':0.49}
        size_hint: (0.7,0.1)
        hint_text : 'password'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'key'
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDFloatingActionButton:
        icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.30}
        user_font_size: '50sp'
        on_press: app.check_username()
#---------------------------------------------------- DOB Screen -------------------------------------------------------------------
<DOB>:
    name:'dob'
    MDLabel:
        text:'Date of Birth'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_y':0.75} 
    MDRaisedButton:
        id:date_picker
        text:'Date Picker'
        user_font_size : '70sp'
        pos_hint : {'center_x':0.5,'center_y':0.6}
        on_press:
            app.show_date_picker()
    MDFloatingActionButton:
        icon:'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size: '45sp'
        on_press: root.manager.current = 'usernamescreen'
    MDFloatingActionButton:
        id: second_disabled
        disabled: True
        icon:'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size: '45sp'
        on_press: root.manager.current = 'mainscreen'
#---------------------------------------------------- Main Screen ----------------------------------------------------------
<MainScreen>:
    name : 'mainscreen'
    FitImage:
        source:'main2.jpg'
        opacity: 0.1
    MDLabel:
        id:profile_name
        text:'main screen'
        font_style : 'H2'
        halign : 'center'
        pos_hint : {'center_y':0.7}
        theme_text_color: 'Custom'
        text_color: 1,1,1,1

    MDRectangleFlatButton:
        text:"Proceed"
        halign: 'center'
        line_color: 1, 1, 1, 1
        pos_hint: {'center_x':.50,'center_y':.25} 
        on_press : root.manager.current = '1s'
#---------------------------------------------------------------------- Contact us ------------------------------------------------------------------------            
<contactus>
    name:'cu'
    MDCard:
        orientation:'vertical'
        padding : '8dp'
        size_hint: None, None
        size: "400dp", "50dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.95}

        MDRoundFlatIconButton:
            text : "social connect"
            icon : 'arrow-left'
            on_press : root.manager.current = '1s'

    MDCard:
        orientation:'vertical'
        padding : '8dp'
        size_hint: None, None
        size: "400dp", "80dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.75}

        MDLabel:
            text: "instagram"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "1dp"

        MDLabel:
            text: "@stocker_handle" 

    MDCard:
        orientation:'vertical'
        padding : '8dp'
        size_hint: None, None
        size: "400dp", "80dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.55}

        MDLabel:
            text: "Email"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "1dp"

        MDLabel:
            text: "stockersmail@gmail.com"  
#------------------------------------------------------------------- Feedback --------------------------------------------------------------           
<Feedback>                
    name: 'fb'

    MDRoundFlatIconButton:
        text : "Back"
        icon : 'arrow-left'
        pos_hint: {'center_x':0.2,'center_y':0.9}
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        on_press : root.manager.current = '1s'
    MDLabel:
        text: 'Rate Our App'
        pos_hint: {'center_x':0.9,'center_y':0.9}
        font_style: 'H4'
        bold: True
        theme_text_color: 'Custom'
        text_color: 231/255,64/255,98/255,1

    MDIconButton:
        id: star1
        icon: "emoticon-devil"
        pos_hint: {'center_x':.2,'center_y':.35}
        theme_text_color: 'Custom'
        text_color: 0,0,0,1
        opacity: 0.5
        on_release: app.select(1)
    MDIconButton:
        id: star2
        icon: "emoticon-confused"
        pos_hint: {'center_x':.35,'center_y':.35}
        theme_text_color: 'Custom'
        text_color: 0,0,0,1
        opacity: 0.5
        on_release: app.select(2)
    MDIconButton:
        id: star3
        icon: "emoticon-happy"
        pos_hint: {'center_x':.50,'center_y':.35}
        theme_text_color: 'Custom'
        text_color: 0,0,0,1
        opacity: 0.5
        on_release: app.select(3)
    MDIconButton:
        id: star4
        icon: "emoticon-excited"
        pos_hint: {'center_x':.65,'center_y':.35}
        theme_text_color: 'Custom'
        text_color: 0,0,0,1
        opacity: 0.5
        on_release: app.select(4)
    MDIconButton:
        id: star5
        icon: "emoticon-cool"
        pos_hint: {'center_x':.8,'center_y':.35}
        theme_text_color: 'Custom'
        text_color: 0,0,0,1
        opacity: 0.5
        on_release: app.select(5)
    MDLabel:
        id: text
        text: ""
        pos_hint: {'center_y':.20}
        halign: 'center'
        font_style: "H5"
        bold: True
        theme_text_color: 'Custom'
        text_color: 67/255,247/255,58/255,1
    MDRaisedButton:
        text: "Submit"
        pos_hint: {'center_x':.5,'center_y':.05}
        md_bg_color: 1,0,0,1
        on_press: app.feedback()

'''
