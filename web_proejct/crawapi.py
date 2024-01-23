import json

import requests
import urllib.request
from urllib.request import urlopen, Request
from urllib.parse import urlencode, urlparse, quote


from bs4 import BeautifulSoup
from datetime import datetime, timezone

from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
from sqlalchemy import select


import reflex as rx
from .model import DailyOTTRank 

#---------------------------------------crawling-------------------------------------

def crawnaver() -> rx.base:
    rank_num:int = 1
    naver_rank:dict = {}
    for i in range(4):
        url:str = f"https://m.search.naver.com/p/csearch/content/nqapirender.nhn?where=nexearch&pkid=702&key=ott_default&u1=netflix&u9={i}&u4=&u2=&u3="
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            data = json.loads(result)["html"]
            soup = BeautifulSoup(data, 'html.parser')
            for y in soup.find_all(class_ = '_text'):
                naver_rank[f"Rank{rank_num}"] = y.text
                rank_num += 1
            # print(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)
    print(naver_rank)
    return naver_rank

def crawfundex() -> rx.base:
    week: datetime.date = datetime.now(timezone.utc).isocalendar().week-1
    year: datetime.date = datetime.now(timezone.utc).year
    
    if week < 10:
        week = "0" + str(week)
    
    wcd: str = str(year)+str(week)
     
    params:dict = {
    "perPage":10,
    "pageoff":0,
    "clsid":"",
    "is_ott":"ott",
    "order":"oqpoint",
    "wcd": wcd,
    "wtype":"week",
    "table":"tvr_week_rank_nor_ott",
    "cat_id":"cat001"
          }
    
    headers: dict = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '258',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'JSESSIONID=98D9B92063857A2F97F401952AF631DC; _ga=GA1.1.161641077.1701936232; _ga_JSWYE0GP3H=GS1.1.1701936232.1.1.1701936279.0.0.0',
    'Host': 'www.gooddata.co.kr',
    'Origin': 'http://www.gooddata.co.kr',
    'Referer' : 'http://www.gooddata.co.kr/fxmain.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 
    'X-Requested-With': 'XMLHttpRequest'
}
    url:str = 'http://www.gooddata.co.kr/select/nowplay.getOqlistNew.do?'

    payload = quote(json.dumps(params, ensure_ascii=False).encode('utf-8'))
    print(payload)
    payload:str = 'param=' + payload

    fundex_rank:dict = {}
    rank_num:int = 1
    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        fundex_result = response.json()
        for i in range(len(fundex_result)):
            fundex_rank[f"Rank{rank_num}"] = fundex_result[i]["pjname"]
            rank_num += 1
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        
    return fundex_rank

def crawjw() -> rx.base:
    
    today : datetime.date = datetime.now(timezone.utc).date()
        
    cookies:dict = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        # 'Cookie': 'jw_id=mEAcn5MtEe6sMKYk9szSug; \
        #     _scid=dd33a3b6-a229-4e85-a36d-1f7507bb5037; \
        #     _scid_r=dd33a3b6-a229-4e85-a36d-1f7507bb5037;',
        'Dnt':'1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    api_url: str = 'https://apis.justwatch.com/graphql'

    variable: dict = {"first":40,"platform":"WEB","popularTitlesSortBy":"POPULAR","sortRandomSeed":0,"offset":None,"creditsRole":"DIRECTOR","after":"","popularTitlesFilter":{"ageCertifications":[],"excludeGenres":[],"excludeProductionCountries":[],"objectTypes":["MOVIE"],"productionCountries":[],"genres":[],"packages":["nfx","prv","dnp","wav","wac","atp","nvs","ply","mbi","gdc","cts","dsv","plx","wow","mgl","bhd","fmz","dkk","trs","daf","hoc","eve","ctx","flb","tak","snx","cla","nfa","cru","tvk","spn","cou","ofb","nhl","tnn","wta","bla","yts","fap","nws","uef","mls","kbs","sbk","mbc","dnf","nlp","twc","erc"],"excludeIrrelevantTitles":False,"presentationTypes":[],"monetizationTypes":[]},"watchNowFilter":{"packages":["nfx","prv","dnp","wav","wac","atp","nvs","ply","mbi","gdc","cts","dsv","plx","wow","mgl","bhd","fmz","dkk","trs","daf","hoc","eve","ctx","flb","tak","snx","cla","nfa","cru","tvk","spn","cou","ofb","nhl","tnn","wta","bla","yts","fap","nws","uef","mls","kbs","sbk","mbc","dnf","nlp","twc","erc"],"monetizationTypes":[]},"language":"ko","country":"KR","allowSponsoredRecommendations":{"appId":"3.8.2-webapp#8682b29","country":"KR","language":"ko","pageType":"VIEW_POPULAR","placement":"POPULAR_VIEW","platform":"WEB"}}

    query: str = '''query GetPopularTitles($allowSponsoredRecommendations: SponsoredRecommendationsInput, $backdropProfile: BackdropProfile, $country: Country!, $first: Int! = 70, $format: ImageFormat, $language: Language!, $platform: Platform! = WEB, $after: String, $popularTitlesFilter: TitleFilter, $popularTitlesSortBy: PopularTitlesSorting! = POPULAR, $profile: PosterProfile, $sortRandomSeed: Int! = 0, $watchNowFilter: WatchNowOfferFilter!, $offset: Int = 0, $creditsRole: CreditRole! = DIRECTOR) {
        popularTitles(
            allowSponsoredRecommendations: $allowSponsoredRecommendations
            country: $country
            filter: $popularTitlesFilter
            first: $first
            sortBy: $popularTitlesSortBy
            sortRandomSeed: $sortRandomSeed
            offset: $offset
            after: $after
        ) {
            edges {
            ...PopularTitleGraphql
            __typename
            }
            pageInfo {
            startCursor
            endCursor
            hasPreviousPage
            hasNextPage
            __typename
            }
            sponsoredAd {
            ...SponsoredAdFragment
            __typename
            }
            totalCount
            __typename
        }
        }

        fragment PopularTitleGraphql on PopularTitlesEdge {
        cursor
        node {
            id
            objectId
            objectType
            content(country: $country, language: $language) {
            title
            fullPath
            scoring {
                imdbVotes
                imdbScore
                tmdbPopularity
                tmdbScore
                __typename
            }
            dailymotionClips: clips(providers: [DAILYMOTION]) {
                sourceUrl
                externalId
                provider
                __typename
            }
            posterUrl(profile: $profile, format: $format)
            ... on MovieOrShowOrSeasonContent {
                backdrops(profile: $backdropProfile, format: $format) {
                backdropUrl
                __typename
                }
                __typename
            }
            isReleased
            credits(role: $creditsRole) {
                name
                personId
                __typename
            }
            scoring {
                imdbVotes
                __typename
            }
            runtime
            genres {
                translation(language: $language)
                __typename
            }
            __typename
            }
            likelistEntry {
            createdAt
            __typename
            }
            dislikelistEntry {
            createdAt
            __typename
            }
            watchlistEntryV2 {
            createdAt
            __typename
            }
            customlistEntries {
            createdAt
            __typename
            }
            freeOffersCount: offerCount(
            country: $country
            platform: $platform
            filter: {monetizationTypes: [FREE]}
            )
            watchNowOffer(country: $country, platform: $platform, filter: $watchNowFilter) {
            id
            standardWebURL
            package {
                id
                packageId
                clearName
                __typename
            }
            retailPrice(language: $language)
            retailPriceValue
            lastChangeRetailPriceValue
            currency
            presentationType
            monetizationType
            availableTo
            __typename
            }
            ... on Movie {
            seenlistEntry {
                createdAt
                __typename
            }
            __typename
            }
            ... on Show {
            tvShowTrackingEntry {
                createdAt
                __typename
            }
            seenState(country: $country) {
                seenEpisodeCount
                progress
                __typename
            }
            __typename
            }
            __typename
        }
        __typename
        }

        fragment SponsoredAdFragment on SponsoredRecommendationAd {
        bidId
        holdoutGroup
        campaign {
            externalTrackers {
            type
            data
            __typename
            }
            hideRatings
            promotionalImageUrl
            watchNowLabel
            watchNowOffer {
            standardWebURL
            presentationType
            monetizationType
            package {
                id
                packageId
                shortName
                clearName
                icon
                __typename
            }
            __typename
            }
            node {
            id
            ... on MovieOrShow {
                content(country: $country, language: $language) {
                fullPath
                posterUrl
                title
                originalReleaseYear
                scoring {
                    imdbScore
                    __typename
                }
                externalIds {
                    imdbId
                    __typename
                }
                backdrops(format: $format, profile: $backdropProfile) {
                    backdropUrl
                    __typename
                }
                isReleased
                __typename
                }
                objectId
                objectType
                offers(country: $country, platform: $platform) {
                monetizationType
                presentationType
                package {
                    id
                    packageId
                    __typename
                }
                id
                __typename
                }
                watchlistEntryV2 {
                createdAt
                __typename
                }
                __typename
            }
            ... on Show {
                seenState(country: $country) {
                seenEpisodeCount
                __typename
                }
                __typename
            }
            __typename
            }
            __typename
        }
        __typename
    }'''
    rs: requests.session = requests.Session()
    post_response = rs.post(api_url, json= {"query": query, "variables": variable}, cookies= cookies)
    get_result:json = json.loads(post_response.text)
    data = get_result["data"]["popularTitles"]["edges"]
    jw_rank:dict = {}
    rank_num: int = 1
    print(data[0]["node"]["content"].keys())
    for i in range(len(data)):
        # print(data["data"]["popularTitles"]["edges"][i]["node"]["content"]['title'])
        jw_rank[f"Rank{rank_num}"] = data[i]["node"]["content"]['title']
        rank_num += 1
    print(jw_rank)
    return jw_rank

async def crawWavve():
    return

async def crawWatcha():
    return

async def crawNetflix():
    return

async def crawTving():
    return

async def crawdisney():
    return

async def crawIMDB():
    return

async def crawTMDB():
    return

async def crawpino():
    return


async def get_dailyrank(rankdate: str):
    with rx.session() as session:
        daily = session.get(DailyOTTRank, rankdate)
    return daily if daily else HTTPException(status_code=404)

async def list_date():
    with rx.session() as session:
        daily = session.scalars(select(DailyOTTRank)).all()
    return daily

def add_rank(data: dict):
    rankdate: str = ""
    data["naver"] = crawnaver()
    data["fundex"] = crawfundex()
    data["jw"] = crawjw()
    with rx.session() as session:
        now: datetime = datetime.now(timezone.utc)
        rankdate = data["rankdate"]
        if not rankdate:
            return HTTPException(status_code=402, detail="Invalid `rankdate`")
        session.add(
            DailyOTTRank(
                rankdate= rankdate,
                created=now,
                updated=now,
                naver=data["naver"],
                jw=data["jw"],
                fundex=data["fundex"],
            )
        )
        session.commit()
    return data


crawling_router = APIRouter(prefix="/DailyOTTRank", tags=["DailyOTTRank"])

crawling_router.add_api_route("", add_rank)
crawling_router.add_api_route("", list_date)
crawling_router.add_api_route("/{rankdate}", get_dailyrank)