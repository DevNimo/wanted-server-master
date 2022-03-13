from app.company.dao import companyDao


def get_all_company_list(lang):
    result = []
    for company in companyDao.get_all():
        result.append({
            'company_code': company.company_code
        })

    return result

