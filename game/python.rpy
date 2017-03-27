###All initialized Python commands go here###

init python:

    ##Import function to get username##
    import getpass
    player_username = str(getpass.getuser())

    ##Change Hyperlinks to not call as sub process##
    def hyperlink_callback(l):
        renpy.jump(l)

    config.hyperlink_callback = hyperlink_callback
