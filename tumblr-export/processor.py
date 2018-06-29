from dateutil import parser
import html
import xml.etree.ElementTree as etree
import re

DATE = re.compile('^.+>((\w{3})dag, .+?)<')

template = """
---
title: "{title}"
date: {date}
campaigndate: {campaign_date}
tags: {tags}
---
{body}
"""


def get_first(el, field):
    try:
        return el.findall(field)[0].text
    except:
        return None


def parse():
    tree = etree.parse('posts.xml')
    root = tree.getroot()

    for child in root[0]:

        title = get_first(child, 'regular-title')
        body = get_first(child, 'regular-body')
        tags = [t.text for t in child.findall('tag') if t.text != 'dnd']

        if not body:
            continue

        try:
            (campaign_date, body) = body.split('\n', 1)
        except:
            campaign_date = None

        if campaign_date:
            try:
                campaign_date = DATE.search(campaign_date)[1]
            except:
                body = campaign_date + body
                campaign_date = None

        body = body.replace('\n', ' ')
        body = body.replace('<p>', '')
        body = body.replace('</p>', '\n\n')

        body = html.unescape(body)

        try:
            slug = child.attrib['slug']
        except:
            slug = None
            print("Skipping {}".format(title))

        date = parser.parse(child.attrib['date'])

        outfile = 'content/posts/{}.md'.format(slug)
        with open(outfile, 'w') as f:
            f.write(template.format(
                campaign_date=campaign_date,
                date=date.isoformat(),
                title=title,
                body=body,
                tags=tags
            ))
        print("Wrote {}".format(outfile))


if __name__ == '__main__':
    parse()
