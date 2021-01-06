**아래의 두코드에 적절한 데코레이터를 작성하여 허용되지 않은 HTTP Method의 경우 405Method Not Allowed 상태코드를 반환 하도록 하시오.**

1.

``` python
from django.views.decorators.http
import require_POST,



@require_http_methods(["GET", "POST"])
@ require_POST
```

