> endpoint parameter

> Jinja for loop

```
<ul>
    {% for card in cards %}
        <li>
            <a href="{{url_for('endpoint_name', index=loop.index0)}}">
                {{card.question}}
            </a>
        </li>
    {% endfor %}
</ul>
```

> Jinja condition, Jinja if

```
{% if index < max_index %}
  <h1> some html</h1>
{% else %}
  <h1> other html </h1>
{% endif %}
```

> Flask abort

```
@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template(card.html, card=card)
    except IndexError:
        abort(404)
```
