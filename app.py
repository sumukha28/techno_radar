import json
import streamlit as st

st.title("Technology Details")

name = st.text_input("Technology Name",placeholder="Enter the Technology name")
ring = st.selectbox("Ring",["Adopt","Trial","Assess","Hold"],index=None,placeholder="Select the Ring")
quadrant = st.selectbox("Quadrant",["Tools","Techniques","Platforms","Languages & Frameworks"],index=None,placeholder="Select the Quadrant")
status = st.selectbox("Status",["True","False"],index=None,placeholder="Select the Status")
owner =  st.text_input("Owners",placeholder="Enter the Owners of the Technology")
contributor = st.text_input("Contributers",placeholder="Enter the Contributors of the Technology")
description = st.text_area("Description",placeholder="Describe your Technology")
projects = st.text_area("Projects",placeholder="Enter the links to the projects")
additional_links = (st.text_area("Additional_links",placeholder="Enter the additional links"))


st.sidebar.markdown("""
## Technology Radar
Technology Radar is a strategic tool used to assess and visualize the maturity, adoption, and relevance of emerging technologies, tools, platforms, and techniques. It is typically organized into quadrants and rings that represent stages of adoption. This radar helps teams make informed technology decisions, encourages innovation, and aligns tech choices with business goals.

### Quadrants
The quadrants are a categorization of the type of blips:
- **Techniques**: These include elements of a software development process, such as experience design; and ways of structuring software, such as microservices.
- **Platforms**: Things that we build software on top of such as mobile technologies like Android, virtual platforms like the JVM, or generic kinds of platforms like hybrid clouds.
- **Tools**: These can be components, such as databases, software development tools, such as versions' control systems; or more generic categories of tools, such as the notion of polyglot persistence.
- **Languages and Frameworks**: These include programming languages like Java and Python but today primarily focus on frameworks like Gradle, Jetpack, and React.js.

### Rings
Radar has four rings, which we'll describe starting from the center:
- **Adopt**: The Adopt ring represents blips that we think you should seriously consider using. We don't say that you should use these for every project; any tool should only be used in an appropriate context. However we do think that a blip in the Adopt ring represents something where there's no doubt that it's proven and mature for use.
- **Trial**: The Trial ring is for blips that we think are ready for use, but not as completely proven as those in the Adopt ring. So for most organizations we think you should use these on a trial basis, to decide whether they should be part of your toolkit. We've used trial blips in production, but we realize that readers may be more cautious than us.
- **Assess**: The Assess ring are things to look at closely, but not necessarily trial yet — unless you think they would be a particularly good fit for you. Typically, blips in the Assess ring are things that we think are interesting and worth keeping an eye on.
- **Hold**: The Hold ring is for things that, even though they may be accepted in the industry, we haven't had a good experience with. Therefore we are calling them out to warn you that you may run into trouble with them as well. Sometimes it means we think they're irredeemably flawed; or just being misused. We do place things in the Hold ring that we wish the industry wouldn't use.

### Status
The Status field is used to highlight which technologies (blips) are new in the current radar edition compared to  previous radar.
- **TRUE**: The technology is appearing for the first time on the radar.
- **FALSE**: The technology already existed in a previous radar version.
""")

if st.button("Submit"):
    with open("input.json","r") as file:
        data = json.load(file)
    
    project_links_list = []
    for line in projects.strip().split('\n'):
        parts = [x.strip() for x in line.split(',')]
        if len(parts) == 2:
            project_links_list.append(parts)
    
    project_links = ", ".join(
        f'<a href="{url}">{label}</a>' for url, label in project_links_list
    )

    additional_links_list = []
    for line in additional_links.strip().split('\n'):
        parts = [x.strip() for x in line.split(',')]
        if len(parts) == 2:
            additional_links_list.append(parts)
    
    links_html = ", ".join(
        f'<a href="{url}">{label}</a>' for url, label in additional_links_list
    )

    new_data = {
        "name": f"{name}",
        "ring": f"{ring}",
        "quadrant": f"{quadrant}",
        "isNew": f"{status}",
        "description": (
            f"<p><strong>Owners: </strong>{owner}</p>\n" 
            f"<p><strong>Contributors:</strong>{contributor}</p>\n" 
            f"<p>{description}</p>\n"
            f"<p><strong>Projects:</strong> {project_links}</p>\n"
            f"<p><strong>Additional links:</strong> {links_html}</p>")
    }

    if any(item['name'] == new_data["name"] for item in data):
        st.error("Data already exists")
    
    else:

        st.write(new_data)
        data.append(new_data)

        with open("input.json","w") as file:
            json.dump(data,file,indent=4)
        
        st.success(f"✅ Data is added to")