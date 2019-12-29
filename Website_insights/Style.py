class Style:
    @staticmethod
    def getWebsiteHeader():
        return '''<div class="" id="header" style="margin-bottom: 90px">
                 <div class="header-w3layouts">
                    <!--//navigation section -->
                    <nav style="background-color:#171C31; color:#aeadaf" class="navbar navbar-expand-lg navbar-light">
                       <div class="hedder-up">
                          <h1><a class="navbar-brand" href="#"> GoBoat</a></h1>
                       </div>
                       <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                       <span class="navbar-toggler-icon"></span>
                       </button>
                       <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
                          <ul class="navbar-nav ">
                          
                          </ul>
                       </div>
                    </nav>
                    <!--//navigation section -->
                    <div class="clearfix"> </div>
                 </div>
                 '''

    @staticmethod
    def getWebsiteCss(file):
       style = open(file, 'r')
       css = style.read()
       style.close()
       return css

