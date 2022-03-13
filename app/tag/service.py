from app.company.service import get_by_company_name
from app.tag.dao import tagDao


def get_compnay_by_tag(tag_name, lang):
    company_result = []
    company_dict = {}
    for company in tagDao.get_compnay_by_tag(tag_name):
        if company.company_code not in company_dict:
            company_dict[company.company_code] = {
                'lang': [company.language],
                'company_name': [company.company_name]
            }
        else:
            company_dict[company.company_code]['lang'].append(company.language)
            company_dict[company.company_code]['company_name'].append(company.company_name)

    for company_code in company_dict:
        lang_list = company_dict[company_code]['lang']
        if lang in lang_list:
            idx = lang_list.index(lang)
        else:
            idx = 0
        company_result.append({
            "company_name": company_dict[company_code]['company_name'][idx]
        })
    return company_result


def tag_update_by_company(company_name, json_data, lang):
    tagDao.tag_update_by_company(company_name, json_data)
    result = get_by_company_name(company_name, lang)
    result['tags'] = sorted(result['tags'], key=lambda x: float(x.split("_")[1]))  # TestCase 에 Sorting때문에 넣음..
    return result


def tag_delete_by_company(company_name, tag_name, lang):
    tagDao.delete_tag_by_company(company_name, tag_name, lang)
    return get_by_company_name(company_name, lang)
