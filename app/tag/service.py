from app.company.dao import companyDao


def get_auto_search_by_company_name(company_name, lang):
    result = []
    for company in companyDao.get_auto_search_by_company_name(company_name, lang):
        result.append({
            'company_name': company.company_name
        })

    return result


def get_by_company_name(company_name, lang):
    result = []
    for company in companyDao.get_by_company_name(company_name, lang):
        result.append({
            'company_name': company.company_name
        })

    return result

