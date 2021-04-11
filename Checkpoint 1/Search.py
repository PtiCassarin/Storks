import twint

# Configure
c = twint.Config()

c.Search = "#pregnancy"
c.Limit = 100
c.Store_csv = True
c.Output = "Test_Config.csv"

twint.run.Search(c)