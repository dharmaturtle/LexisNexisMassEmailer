#!/usr/bin/python
# -*- coding: utf-8 -*-

import pp, socket, re, os, sys
from ast import literal_eval

#DateRange
dater1 = []
dater2 = []
dater3 = []
dater4 = []
file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'
file4 = '4.txt'
with open(file1,'rU') as s:
	for line in s:
		r = re.search('(.*?),(\(.*?\))',line)
		dater1.append((r.group(1),literal_eval(r.group(2))))
with open(file2,'rU') as s:
	for line in s:
		r = re.search('(.*?),(\(.*?\))',line)
		dater2.append((r.group(1),literal_eval(r.group(2))))
with open(file3,'rU') as s:
	for line in s:
		r = re.search('(.*?),(\(.*?\))',line)
		dater3.append((r.group(1),literal_eval(r.group(2))))
with open(file4,'rU') as s:
	for line in s:
		r = re.search('(.*?),(\(.*?\))',line)
		dater4.append((r.group(1),literal_eval(r.group(2))))

path = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),) + "\\"

# wrap everything inside function
def lexisnexis(core_number, dates, path):
	note_in_email = "Version or iteration number/identifier goes here"

	# rename imported modules
	webdriver = selenium.webdriver
	By = selenium.webdriver.common.by.By
	WebDriverWait = selenium.webdriver.support.ui.WebDriverWait
	EC = selenium.webdriver.support.expected_conditions
	NoSuchElementException = selenium.common.exceptions.NoSuchElementException
	WebDriverException = selenium.common.exceptions.WebDriverException
	TimeoutException = selenium.common.exceptions.TimeoutException

	log_sum = open(path + "log_sum_{} {}.txt".format(str(core_number),note_in_email), mode = "w", buffering = 0)
	log_err = open(path + "log_err_{} {}.txt".format(str(core_number),note_in_email), mode = "w", buffering = 0)

	# create function to handle NoSuchElementException
	def exists_by_xpath(xpath):
		try:
			browser.find_element_by_xpath(xpath)
		except NoSuchElementException:
			return False
		return True

	# create function to handle WebDriverException
	def find_and_click(browserfind):
		try:
			browserfind.click()
		except WebDriverException:
			log_err.write(countries[country_code] + "," + str(date) + "," + "error: WebDriverException, on {}".format(str(browserfind)) + "\n")
			time.sleep(5)

	def exists_by_css_selector(css_selector):
		try:
			browser.find_element_by_css_selector(css_selector)
		except NoSuchElementException:
			return False
		return True

	# dict of country codes (LexisNexis codes) and country names
	countries = {'(#GC519#)': 'Botswana', '(#GC314#)': 'Belgium', '(#GC500#)': 'Angola', '(#GC349#)': 'Kuwait', '(#GC562#)': 'TrinidadAndTobago', '(#GC379#)': 'Nicaragua', '(#GC510#)': 'AntiguaAndBarbuda', '(#ST0009XYU#)': 'Kosovo', '(#GC321#)': 'Italy', '(#GC549#)': 'Mongolia', '(#GC574#)': 'Kyrgyzstan', '(#GC319#)': 'Greece', '(#GC688#)': 'Tuvalu', '(#GC571#)': 'Estonia', '(#GC360#)': 'Morocco', '(#GC564#)': 'Vanuatu', '(#GC698#)': 'Mali', '(#GC329#)': 'UnitedKingdom', '(#ST0009QYL#)': 'Montenegro', '(#GC378#)': 'Nepal', '(#GC674#)': 'SanMarino', '(#GC365#)': 'Haiti', '(#GC335#)': 'SaudiArabia', '(#GC576#)': 'Lithuania', '(#GC387#)': 'IvoryCoast', '(#GC541#)': 'Madagascar', '(#GC377#)': 'Namibia', '(#GC301#)': 'Australia', '(#GC577#)': 'Moldova', '(#GC597#)': 'SolomonIslands', '(#GC368#)': 'Iran', '(#GC300#)': 'Vatican', '(#GC336#)': 'SouthAfrica', '(#GC367#)': 'PapuaNewGuinea', '(#GC333#)': 'Israel', '(#GC385#)': 'Vietnam', '(#GC366#)': 'Honduras', '(#GC579#)': 'Tajikistan', '(#GC384#)': 'Tunisia', '(#GC542#)': 'Malawi', '(#GC334#)': 'Nigeria', '(#GC592#)': 'Malta', '(#GC656#)': 'Montserrat', '(#GC372#)': 'Laos', '(#GC340#)': 'Chile', '(#GC394#)': 'CongoKinshasa', '(#GC556#)': 'Seychelles', '(#GC312#)': 'Taiwan', '(#GC358#)': 'Iraq', '(#GC313#)': 'Thailand', '(#GC343#)': 'UnitedStates', '(#GC700#)': 'Eritrea', '(#GC370#)': 'Jordan', '(#GC346#)': 'Austria', '(#GC598#)': 'Swaziland', '(#GC396#)': 'Zimbabwe', '(#GC371#)': 'NorthKorea', '(#GC554#)': 'Rwanda', '(#GC529#)': 'Cyprus', '(#GC397#)': 'Iceland', '(#GC555#)': 'Senegal', '(#GC341#)': 'Colombia', '(#GC586#)': 'Macedonia', '(#GC353#)': 'Peru', '(#GC399#)': 'Albania', '(#GC327#)': 'Switzerland', '(#GC585#)': 'Croatia', '(#GC382#)': 'Sudan', '(#GC326#)': 'Sweden', '(#GC350#)': 'Libya', '(#GC383#)': 'Tanzania', '(#GC355#)': 'Bulgaria', '(#GC310#)': 'Philippines', '(#GC587#)': 'Kiribati', '(#GC352#)': 'Panama', '(#GC527#)': 'Comoros', '(#GC509#)': 'Andorra', '(#GC531#)': 'EquatorialGuinea', '(#GC338#)': 'Brazil', '(#GC391#)': 'Guinea', '(#GC339#)': 'Canada', '(#GC525#)': 'CentralAfricanRepublic', '(#GC580#)': 'Turkmenistan', '(#GC524#)': 'CapeVerde', '(#GC325#)': 'Spain', '(#GC306#)': 'Japan', '(#GC516#)': 'Belize', '(#GC504#)': 'ElSalvador', '(#GC631#)': 'Dominica', '(#GC539#)': 'Lesotho', '(#GC309#)': 'Pakistan', '(#GC386#)': 'Cameroon', '(#GC536#)': 'CzechRepublic', '(#GC514#)': 'Bangladesh', '(#GC537#)': 'GuineaBissau', '(#GC515#)': 'Barbados', '(#GC501#)': 'Bolivia', '(#GC315#)': 'Denmark', '(#GC563#)': 'Uganda', '(#GC308#)': 'Malaysia', '(#GC503#)': 'Cuba', '(#GC699#)': 'EastTimor', '(#GC561#)': 'Tonga', '(#GC502#)': 'Cambodia', '(#GC560#)': 'Togo', '(#GC651#)': 'Slovakia', '(#GC320#)': 'Ireland', '(#GC548#)': 'Monaco', '(#GC570#)': 'Belarus', '(#GC513#)': 'Bahrain', '(#GC601#)': 'Samoa', '(#GC369#)': 'Jamaica', '(#GC572#)': 'Georgia', '(#ST0009QYK#)': 'Serbia', '(#GC573#)': 'Kazakhstan', '(#GC318#)': 'Germany', '(#GC363#)': 'Syria', '(#GC362#)': 'Romania', '(#GC328#)': 'Turkey', '(#GC608#)': 'Bhutan', '(#GC566#)': 'Yemen', '(#GC558#)': 'Somalia', '(#GC361#)': 'Poland', '(#GC569#)': 'Azerbaijan', '(#GC673#)': 'SaintVincentAndTheGrenadines', '(#GC568#)': 'Armenia', '(#GC552#)': 'Qatar', '(#GC374#)': 'Liberia', '(#GC578#)': 'Russia', '(#GC375#)': 'Luxembourg', '(#GC337#)': 'Argentina', '(#GC547#)': 'Mauritius', '(#GC575#)': 'Latvia', '(#GC345#)': 'Algeria', '(#GC546#)': 'Mauritania', '(#GC376#)': 'Mozambique', '(#GC302#)': 'China', '(#GC559#)': 'Suriname', '(#GC660#)': 'Niue', '(#GC364#)': 'Uruguay', '(#GC332#)': 'Egypt', '(#GC665#)': 'Palau', '(#GC540#)': 'Liechtenstein', '(#GC389#)': 'DominicanRepublic', '(#GC359#)': 'Kenya', '(#GC671#)': 'SaintLucia', '(#GC388#)': 'CostaRica', '(#GC342#)': 'Mexico', '(#GC670#)': 'SaintKittsAndNevis', '(#GC550#)': 'Nauru', '(#GC551#)': 'Niger', '(#GC311#)': 'Singapore', '(#GC344#)': 'Venezuela', '(#GC596#)': 'SaoTomeAndPrincipe', '(#GC390#)': 'Gabon', '(#GC373#)': 'Lebanon', '(#GC305#)': 'Indonesia', '(#GC347#)': 'Ecuador', '(#GC395#)': 'Zambia', '(#GC304#)': 'India', '(#GC557#)': 'SierraLeone', '(#GC521#)': 'BurkinaFaso', '(#GC584#)': 'Slovenia', '(#GC381#)': 'SriLanka', '(#GC520#)': 'Brunei', '(#GC351#)': 'NewZealand', '(#GC380#)': 'Paraguay', '(#GC583#)': 'BosniaAndHerzegovina', '(#GC523#)': 'Burundi', '(#GC324#)': 'Portugal', '(#GC357#)': 'Hungary', '(#GC538#)': 'Guyana', '(#GC316#)': 'Finland', '(#GC354#)': 'UnitedArabEmirates', '(#GC317#)': 'France', '(#GC532#)': 'Fiji', '(#GC392#)': 'Oman', '(#GC533#)': 'Gambia', '(#GC528#)': 'CongoBrazzaville', '(#GC530#)': 'Djibouti', '(#GC582#)': 'Uzbekistan', '(#GC526#)': 'Chad', '(#GC323#)': 'Norway', '(#GC581#)': 'Ukraine', '(#GC508#)': 'Afghanistan', '(#GC322#)': 'Netherlands', '(#GC507#)': 'Guatemala', '(#GC506#)': 'Ghana', '(#GC307#)': 'SouthKorea', '(#GC522#)': 'Myanmar', '(#GC505#)': 'Ethiopia', '(#GC512#)': 'Bahamas', '(#ST000CMCM#)': 'Micronesia', '(#GC535#)': 'Grenada', '(#GC517#)': 'Benin'}
	inv = {v:k for k, v in countries.items()}

	# start webdriver (PhantomJS binary must be on path)
	browser = webdriver.PhantomJS(executable_path = path + "phantomjs\\phantomjs.exe")
	browser.get("http://www.lexisnexis.com/hottopics/lnacademic/?verb=sf&sfi=AC00NBGenSrch")

	# loop over every country
	browser.implicitly_wait(30)
	for x in dates:
		try:
			country_code = inv[x[0]]
			date = x[1]
			
			# gmail has rate limits, both recieving and downloading, so this is to help distribute the data
			rand = random.randint(0,9)
			if rand == 1: email = "email1@gmail.com"
			elif rand == 2: email = "email2@gmail.com"
			elif rand == 3: email = "email3@gmail.com"
			elif rand == 4: email = "email4@gmail.com"
			elif rand == 5: email = "email5@gmail.com"
			elif rand == 6: email = "email6@gmail.com"
			elif rand == 7: email = "email7@gmail.com"
			elif rand == 8: email = "email8@gmail.com"
			elif rand == 9: email = "email9@gmail.com"
			else:
				email = "email10@gmail.com"

			# input search terms
			searchwindow = browser.window_handles[0]
			browser.switch_to_window(searchwindow)
			browser.switch_to_frame("mainFrame")
			browser.find_element_by_id("terms").clear()
			browser.find_element_by_id("terms").send_keys("((#STX002003#) OR (#STX000873#) OR (#ST0009J49#) OR (#STX000271#) OR (#ST0008ZBZ#)) and {}".format(country_code))

			# select date range
			find_and_click(browser.find_element_by_xpath("//select[@name='dateSelector1']/option[contains(text(), 'Date is between')]"))
			browser.find_element_by_id("fromDate1").clear()
			browser.find_element_by_id("fromDate1").send_keys(date[0])
			browser.find_element_by_id("toDate1").clear()
			browser.find_element_by_id("toDate1").send_keys(date[1])

			# select source
			find_and_click(browser.find_element_by_xpath("//select[@id='byType']/option[text()='All News (English)']"))

			# submit search
			try:
				browser.find_element_by_css_selector("input[type=\"submit\"]").click()
			except socket.error:
				log_err.write(countries[country_code] + "," + str(date) + "," + "error: socket.error, on processor{}, at {}".format(str(core_number), time.strftime("%X %x") + "\n"))
				print "Processor{} closing due to socket error (see log for details).".format(str(core_number))
				browser.close()
				browser.quit()

			# navigate to main frame
			browser.switch_to_default_content()
			browser.switch_to_frame("mainFrame")
			browser.implicitly_wait(30)

			# if 0 results, call next; if 3000+ results, click on "Retrieve Results"
			move_on = True
			if exists_by_xpath("//frame[contains(@name, 'fr_resultsNav')]") == False:
				move_on = False
				browser.implicitly_wait(30)
				if exists_by_css_selector("img[alt=\"Retrieve Results\"]") == True:
					log_err.write(countries[country_code] + "," + str(date) + "," + "error: Too many results!\n")
				elif exists_by_css_selector("img[alt=\"Warning\"]") == True:
					log_sum.write(countries[country_code] + "," + str(date) + "," + "0 results" + "\n")
				else:
					log_err.write(countries[country_code] + "," + str(date) + "," + "Neither 0 results nor 3000+ results" + "\n")
				backwindow = browser.window_handles[0]
				browser.switch_to_window(backwindow)
				browser.switch_to_frame("topFrame")
				find_and_click(browser.find_element_by_link_text("Edit Search"))
				continue

			# else, email results
			if move_on == True:
				browser.implicitly_wait(30)
				framelist = browser.find_elements_by_xpath("//frame[contains(@name, 'fr_resultsNav')]")
				framename = framelist[0].get_attribute("name")
				browser.switch_to_frame(framename)
				total = int(browser.find_element_by_name("totalDocsInResult").get_attribute("value"))

				# if one result
				if total == 1:
					find_and_click(browser.find_element_by_css_selector("img[alt=\"Email Documents\"]"))
					browser.switch_to_default_content()
					browser.switch_to_window(browser.window_handles[1])
					browser.implicitly_wait(0)

					# if black screen appears, call next
					if exists_by_xpath("//select[@id='delFmt']/option[text()='Text']") == False:
						browser.implicitly_wait(30)
						browser.close()
						backwindow = browser.window_handles[0]
						browser.switch_to_window(backwindow)
						browser.switch_to_frame("topFrame")
						find_and_click(browser.find_element_by_link_text("Edit Search"))
						log_err.write(countries[country_code] + "," + str(date) + "," + "error: black screen 1" + "\n")
						continue

					# else, email result
					else:
						browser.implicitly_wait(30)
						if browser.find_element_by_id("docnewpg").is_selected() == True:
							find_and_click(browser.find_element_by_id("docnewpg"))
						if browser.find_element_by_id("termBold").is_selected() == True:
							find_and_click(browser.find_element_by_id("termBold"))
						find_and_click(browser.find_element_by_xpath("//select[@id='sendAs']/option[text()='Attachment']"))
						find_and_click(browser.find_element_by_xpath("//select[@id='delFmt']/option[text()='Text']"))
						browser.find_element_by_name("emailTo").clear()
						browser.find_element_by_name("emailTo").send_keys(email)
						browser.find_element_by_id("emailNote").clear()
						browser.find_element_by_id("emailNote").send_keys("{}_{} {}".format(countries[country_code], date, note_in_email))
						find_and_click(browser.find_element_by_css_selector("img[alt=\"Send\"]"))
						try:
							element = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt=\"Close Window\"]")))
						except TimeoutException:
							log_err.write(countries[country_code] + "," + str(date) + "," + "error: TimeoutException" + "\n")
							time.sleep(30)
						browser.close()
						log_sum.write(countries[country_code] + "," + str(date) + "," + email + ",1\n")

				# if it takes one email
				elif total > 1 and total < 501:
					browser.implicitly_wait(30)
					find_and_click(browser.find_element_by_css_selector("img[alt=\"Email Documents\"]"))
					browser.switch_to_default_content()
					browser.switch_to_window(browser.window_handles[1])

					# if black screen appears, call next
					if exists_by_xpath("//select[@id='delFmt']/option[text()='Text']") == False:
						browser.implicitly_wait(30)
						browser.close()
						backwindow = browser.window_handles[0]
						browser.switch_to_window(backwindow)
						browser.switch_to_frame("topFrame")
						find_and_click(browser.find_element_by_link_text("Edit Search"))
						log_err.write(countries[country_code] + "," + str(date) + "," + "error: black screen 2" + "\n")
						continue

					# else, email all results at once
					else:
						browser.implicitly_wait(30)
						if browser.find_element_by_id("docnewpg").is_selected() == True:
							find_and_click(browser.find_element_by_id("docnewpg"))
						if browser.find_element_by_id("termBold").is_selected() == True:
							find_and_click(browser.find_element_by_id("termBold"))
						find_and_click(browser.find_element_by_xpath("//select[@id='sendAs']/option[text()='Attachment']"))
						find_and_click(browser.find_element_by_xpath("//select[@id='delFmt']/option[text()='Text']"))
						browser.find_element_by_name("emailTo").clear()
						browser.find_element_by_name("emailTo").send_keys(email)
						browser.find_element_by_id("emailNote").clear()
						browser.find_element_by_id("emailNote").send_keys("{}_{} {}".format(countries[country_code], date, note_in_email))
						find_and_click(browser.find_element_by_css_selector("img[alt=\"Send\"]"))
						try:
							element = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt=\"Close Window\"]")))
						except TimeoutException:
							log_err.write(countries[country_code] + "," + str(date) + "," + "error: TimeoutException" + "\n")
							time.sleep(30)
						browser.close()
						log_sum.write(countries[country_code] + "," + str(date) + "," + email + ",1-" + str(total) + "\n")

				# if it takes multiple emails
				elif total > 500:
					initial = 1
					final = 500
					black_screen = 0
					batch = 0
					while final <= total and final >= initial and black_screen < 2:
						browser.implicitly_wait(30)
						find_and_click(browser.find_element_by_css_selector("img[alt=\"Email Documents\"]"))
						browser.switch_to_default_content()
						browser.switch_to_window(browser.window_handles[1])

						# if black screen appears, try once more
						if exists_by_xpath("//select[@id='delFmt']/option[text()='Text']") == False:
							browser.implicitly_wait(30)
							browser.close()
							backwindow = browser.window_handles[0]
							browser.switch_to_window(backwindow)
							browser.switch_to_default_content()
							browser.switch_to_frame("mainFrame")
							framelist = browser.find_elements_by_xpath("//frame[contains(@name, 'fr_resultsNav')]")
							framename = framelist[0].get_attribute("name")
							browser.switch_to_frame(framename)
							black_screen += 1
							log_err.write(countries[country_code] + "," + str(date) + "," + "error: black screen 3" + "\n")
							continue

						# else, email 500 results at a time
						else:
							browser.implicitly_wait(30)
							batch += 1
							if browser.find_element_by_id("docnewpg").is_selected() == True:
								find_and_click(browser.find_element_by_id("docnewpg"))
							if browser.find_element_by_id("termBold").is_selected() == True:
								find_and_click(browser.find_element_by_id("termBold"))
							find_and_click(browser.find_element_by_xpath("//select[@id='sendAs']/option[text()='Attachment']"))
							find_and_click(browser.find_element_by_xpath("//select[@id='delFmt']/option[text()='Text']"))
							browser.find_element_by_name("emailTo").clear()
							browser.find_element_by_name("emailTo").send_keys(email)
							browser.find_element_by_id("emailNote").clear()
							browser.find_element_by_id("emailNote").send_keys("{}_{}_{} {}".format(countries[country_code], str(batch), date, note_in_email))
							find_and_click(browser.find_element_by_id("sel"))
							browser.find_element_by_id("rangetextbox").clear()
							browser.find_element_by_id("rangetextbox").send_keys("{}-{}".format(initial, final))
							find_and_click(browser.find_element_by_css_selector("img[alt=\"Send\"]"))
							try:
								element = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt=\"Close Window\"]")))
							except TimeoutException:
								log_err.write(countries[country_code] + "," + str(date) + "," + "error: TimeoutException" + "\n")
								time.sleep(30)
							browser.close()
							backwindow = browser.window_handles[0]
							browser.switch_to_window(backwindow)
							browser.switch_to_default_content()
							browser.switch_to_frame("mainFrame")
							framelist = browser.find_elements_by_xpath("//frame[contains(@name, 'fr_resultsNav')]")
							framename = framelist[0].get_attribute("name")
							browser.switch_to_frame(framename)
							log_sum.write(countries[country_code] + "," + str(batch) + "," + str(date) + "," + email + "," + str(initial) + "-" + str(final) + " of " + str(total) + "\n")

							# update initial and final documents
							initial += 500
							if final + 500 > total:
								final = total
							else:
								final += 500
			# start over
			backwindow = browser.window_handles[0]
			browser.switch_to_window(backwindow)
			browser.switch_to_frame("topFrame")
			find_and_click(browser.find_element_by_link_text("Edit Search"))

		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			time.sleep(30)
			try:
				log_err.write(countries[country_code] + "," + str(date) + "," + "error: Unknown! \n" + str(traceback.format_exc()) + "\n" + str(sys.exc_info()) + "\n\n")
			except:
				log_err.write(countries[country_code] + "," + str(date) + "," + "error: Unknown!\n\n")

	# exit
	print "Processor{} finished".format(str(core_number))
	browser.close()
	browser.quit()
	log_sum.close()
	log_err.close()

# modules to import through PP
modules_to_import = ("selenium.webdriver", "selenium.webdriver.common.by", "selenium.webdriver.support.ui", "selenium.webdriver.support.expected_conditions","selenium.common.exceptions", "socket", "time", "sys", "os", "traceback","re","random")

# parallelize the job and execute
job_server = pp.Server()
core1  = job_server.submit(func = lexisnexis, args = (1 , dater1 , path), modules = modules_to_import)
core2  = job_server.submit(func = lexisnexis, args = (2 , dater2 , path), modules = modules_to_import)
core3  = job_server.submit(func = lexisnexis, args = (3 , dater3 , path), modules = modules_to_import)
core4  = job_server.submit(func = lexisnexis, args = (4 , dater4 , path), modules = modules_to_import)

# collect PP output and stats
output = [core1(), core2(), core3(), core4()]
job_server.print_stats()