from django.db import connection

class QueryStatistic(object):
    def process_response(self,request,response):
        queries = connection.queries
        time = 0
        count = len(queries)
        for query in queries:
            time += float(query['time'])
        if 'content="text/html' in response.content:
            response.content = response.content.replace(
                '</body>',
                'Count of queries: '+str(count)+'; time: '+str(time)+'s</body>'
                )
        return response
