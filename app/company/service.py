from app.company.dao import companyDao
from app.tag.dao import tagDao


def get_auto_search_by_company_name(company_name, lang):
    result = []
    for company in companyDao.get_auto_search_by_company_name(company_name, lang):
        result.append({
            'company_name': company.company_name
        })

    return result


def get_by_company_name(company_name, lang):
    result = {
        'tags':[]
    }
    for company in companyDao.get_by_company_name(company_name, lang):
        result['company_name'] = company.company_name

    for tag_name in tagDao.get_by_company_name(company_name, lang):
        result['tags'].append(tag_name.tag_name)
    return result


def create_new_company(json_data, lang):
    company_name = companyDao.new_company(json_data, lang)

    result = {
        'tags':[]
    }
    for company in companyDao.get_by_company_name(company_name, lang):
        result['company_name'] = company.company_name

    for tag_name in tagDao.get_by_company_name(company_name, lang):
        result['tags'].append(tag_name.tag_name)
    return result
