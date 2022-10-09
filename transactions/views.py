from rest_framework import generics
from rest_framework.views import Response, status
from .serializers import TransactionSerializer, UploadSerializer
from rest_framework import parsers
import ipdb

class PlainTextParser(parsers.BaseParser):
    """
    Plain text parser.
    """
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream.read()

class UploadView(generics.CreateAPIView):
    serializer_class = UploadSerializer

    def create(self, request):
        response = []

        uploaded_file = request.FILES.get("uploaded_file")
        content = [line.decode("utf-8") for line in uploaded_file]
        # ipdb.set_trace()

        for line in content:
            # ipdb.set_trace()
            parsed_data = {
                'transaction_type': line[:1],
                'date': line[1:5] + '-' +
                        line[5:7] + '-' +
                        line[7:9] + 'T' +
                        line[42:44] + ':' +
                        line[44:46] + ':' +
                        line[46:48],
                'amount': float(line[9:19])/100,
                'cpf': line[19:30],
                'card': line[30:42],
                'owner': line[48:62].strip(),
                'store_name': line[62:81].strip(),
            }

            serializer = TransactionSerializer(data=parsed_data)

            serializer.is_valid(raise_exception=True)

            serializer.save()

            response.append(serializer.data)

        return Response({"content": response}, status.HTTP_201_CREATED)














