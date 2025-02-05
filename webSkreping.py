import time
from seleniumbase import SB
import configURL

def fetch_data_from_url_latvia():
    data = {}

    with SB(uc=True) as sb:
        sb.open(configURL.URLS["authorisationOfElectronicMoneyInstitutionsUrl"])
        
        #Opening of the FIRST element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-1')]")
        sb.click("//div[contains(@id, 'ex-1-1')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[1]/h3", timeout=10)
        data["titleFromLicenseOfAnElectronicMoneyInstitutionEMI"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[1]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[1]/div", timeout=10)
        data["textFromLicenseOfAnElectronicMoneyInstitutionEMI"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[1]/div")

        #Opening of the SECOND element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-2')]")
        sb.click("//div[contains(@id, 'ex-1-2')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[2]/h3", timeout=10)
        data["titleLicenceOfAnElectronicMoneyInstitutionToEngageInRestrictedActivities"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[2]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[2]/div", timeout=10)
        data["textLicenceOfAnElectronicMoneyInstitutionToEngageInRestrictedActivities"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[2]/div")

        #Opening of the THIRD element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-3')]")
        sb.click("//div[contains(@id, 'ex-1-3')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[3]/h3", timeout=10)
        data["titleAuthorisationProcess"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[3]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[3]/div", timeout=10)
        data["textAuthorisationProcess"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[3]/div")

        #Opening of the FOURTH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-4')]")
        sb.click("//div[contains(@id, 'ex-1-4')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[4]/h3", timeout=10)
        data["titleStatutoryTimeframe"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[4]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[4]/div", timeout=10)
        data["textStatutoryTimeframe"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[4]/div")

        #Opening of the FIFTH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-5')]")
        sb.click("//div[contains(@id, 'ex-1-5')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[5]/h3", timeout=10)
        data["titleEMILicenceFee"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[5]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[5]/div", timeout=10)
        data["textEMILicenceFee"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[5]/div")

        #Opening of the SIXTH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-6')]")
        sb.click("//div[contains(@id, 'ex-1-6')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[6]/h3", timeout=10)
        data["titleKeyRequirementsForAnEMIBeingEstablishedOrAuthorised"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[6]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[6]/div", timeout=10)
        data["textKeyRequirementsForAnEMIBeingEstablishedOrAuthorised"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[6]/div")

        #Opening of the SEVENTH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-7')]")
        sb.click("//div[contains(@id, 'ex-1-7')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[7]/h3", timeout=10)
        data["titleAssessmentOfSubmittedDocuments"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[7]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[7]/div", timeout=10)
        data["textAssessmentOfSubmittedDocuments"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[7]/div")

        #Opening of the EIGHTH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-8')]")
        sb.click("//div[contains(@id, 'ex-1-8')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[8]/h3", timeout=10)
        data["titleDocumentsAndInformationToBeSubmittedToTheBankOfLithuania"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[8]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[8]/div", timeout=10)
        data["textDocumentsAndInformationToBeSubmittedToTheBankOfLithuania"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[8]/div")

        #Opening of the NINETH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-9')]")
        sb.click("//div[contains(@id, 'ex-1-9')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[9]/h3", timeout=10)
        data["titleDocumentsAndInformationToBeSubmittedToTheBankOfLithuaniaInOrderToBeGrantedAnEMILicenceToEngageInRestrictedActivities"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[9]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[9]/div", timeout=10)
        data["textDocumentsAndInformationToBeSubmittedToTheBankOfLithuaniaInOrderToBeGrantedAnEMILicenceToEngageInRestrictedActivities"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[9]/div")

        #Opening of the TENTH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-10')]")
        sb.click("//div[contains(@id, 'ex-1-10')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[10]/h3", timeout=10)
        data["titleLawsAndLegalActsRegulatingTheActivities"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[10]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[10]/div", timeout=10)
        data["textLawsAndLegalActsRegulatingTheActivities"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[10]/div")


        # Next URL
        sb.open(configURL.URLS["authorisationOfPaymentInstitutionsUrl"])

        #Opening of the FIRST element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-1')]")
        sb.click("//div[contains(@id, 'ex-1-1')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[1]/h3", timeout=10)
        data["titleLicenceOfAPaymentInstitution"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[1]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[1]/div", timeout=10)
        data["textLicenceOfAPaymentInstitution"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[1]/div")

        #Opening of the SECOND element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-2')]")
        sb.click("//div[contains(@id, 'ex-1-2')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[2]/h3", timeout=10)
        data["titleLicenceOfAPaymentInstitutionToEngageInRestrictedActivities"]= sb.get_text("/html/body/section/div/div[2]/div/div/div[2]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[2]/div", timeout=10)
        data["textLicenceOfAPaymentInstitutionToEngageInRestrictedActivities"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[2]/div")

        #Opening of the THIRD element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-3')]")
        sb.click("//div[contains(@id, 'ex-1-3')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[3]/h3", timeout=10)
        data["titleTheRequirementForTheMinimumInitialCapitalOfAPaymentInstitution"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[3]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[3]/div", timeout=10)
        data["textTheRequirementForTheMinimumInitialCapitalOfAPaymentInstitution"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[3]/div")

        #Opening of the FOURTH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-4')]")
        sb.click("//div[contains(@id, 'ex-1-4')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[4]/h3", timeout=10)
        data["titleAuthorisationProcess"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[4]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[4]/div", timeout=10)
        data["textAuthorisationProcess"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[4]/div")

        #Opening of the FIFTH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-5')]")
        sb.click("//div[contains(@id, 'ex-1-5')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[5]/h3", timeout=10)
        data["titleStatutoryTimeframe"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[5]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[5]/div", timeout=10)
        data["textStatutoryTimeframe"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[5]/div")

        #Opening of the SIXTH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-6')]")
        sb.click("//div[contains(@id, 'ex-1-6')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[6]/h3", timeout=10)
        data["titlePaymentInstitutionLicenceFee"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[6]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[6]/div", timeout=10)
        data["textPaymentInstitutionLicenceFee"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[6]/div")

        #Opening of the SEVENTH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-7')]")
        sb.click("//div[contains(@id, 'ex-1-7')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[7]/h3", timeout=10)
        data["titleKeyRequirementsForAPaymentInstitutionBeingEstablishedOrAuthorised"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[7]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[7]/div", timeout=10)
        data["textKeyRequirementsForAPaymentInstitutionBeingEstablishedOrAuthorised"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[7]/div")

        #Opening of the EIGHTH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-8')]")
        sb.click("//div[contains(@id, 'ex-1-8')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[8]/h3", timeout=10)
        data["titleAssessmentOfSubmittedDocuments"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[8]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[8]/div", timeout=10)
        data["textAssessmentOfSubmittedDocuments"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[8]/div")

        #Opening of the NINETH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-9')]")
        sb.click("//div[contains(@id, 'ex-1-9')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[9]/h3", timeout=10)
        data["titleDocumentsAndInformationToBeSubmittedToTheBankOfLithuaniaInOrderToBeGrantedAPaymentInstitutionLicence"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[9]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[9]/div", timeout=10)
        data["textDocumentsAndInformationToBeSubmittedToTheBankOfLithuaniaInOrderToBeGrantedAPaymentInstitutionLicence"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[9]/div")

        #Opening of the TENTH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-10')]")
        sb.click("//div[contains(@id, 'ex-1-10')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[10]/h3", timeout=10)
        data["titleDocumentsAndInformationToBeSubmittedToTheBankOfLithuaniaInOrderToBeGrantedALicenceOfAPaymentInstitutionToEngageInRestrictedActivities"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[10]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[10]/div", timeout=10)
        data["textDocumentsAndInformationToBeSubmittedToTheBankOfLithuaniaInOrderToBeGrantedALicenceOfAPaymentInstitutionToEngageInRestrictedActivities"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[10]/div")

        #Opening of the ELEVENTH element
        sb.wait_for_element_clickable("//div[contains(@id, 'ex-1-11')]")
        sb.click("//div[contains(@id, 'ex-1-11')]") 

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[11]/h3", timeout=10)
        data["titleLawsAndLegalActsRegulatingTheActivitiesAndAuthorisationOfPaymentInstitutions"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[11]/h3")

        sb.wait_for_element_visible("/html/body/section/div/div[2]/div/div/div[11]/div", timeout=10)
        data["textLawsAndLegalActsRegulatingTheActivitiesAndAuthorisationOfPaymentInstitutions"] = sb.get_text("/html/body/section/div/div[2]/div/div/div[11]/div")

        time.sleep(200) 
fetch_data_from_url_latvia()