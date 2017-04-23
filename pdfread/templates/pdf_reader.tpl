<html>
  <head>
    {% load static from staticfiles %}
    <script src="{% static 'js/pdf.js' %}"></script>
    <script src="{% static 'js/pdf_reader.js' %}"></script>

    <style>
      .pdf-upload {
          height: auto;
          width: 300px;
          margin: 0 auto;
          background: #F2EEEE;
          padding-bottom: 10px;
          padding-left: 20px;
          padding-right: 10px;
      }
      .pdf-upload input {
         margin-top: 5px;
         margin-bottom: 5px;
         display: flex
      }

      .errorlist li {
          color: red;
      }
    </style>
  </head>
  <body>
    <div class="pdf-upload">
      <div id="msg-ele">
          {% if success %}
              <p style="color: green">{{success}}</p>
          {% endif %}
          {% if failure %}
              <p style="color: red">{{failure}}</p>
          {% endif %}
          
      </div>
      <form action="/" method="post" enctype="multipart/form-data" id="id-pdf-form"
          onsubmit="event.preventDefault(); validatePDF();">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Submit"/>
      </form>
    </div>
  </body>
</html>
