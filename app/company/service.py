from app.company.dao import companyDao


def get_all_company_list(company_name, lang):
    result = []
    for company in companyDao.get_auto_search_by_company_name(company_name):
        result.append({
            'company_code': company.company_code
        })

    return result

